# Helper functions

from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import re

# Load environment variables
load_dotenv()

# Logs in user to CS50.me using Github Oauth
def get_scores():
    
    login_url = "https://github.com/login?client_id=4641d3506c478b0419d5&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D4641d3506c478b0419d5"
    "%26scope%3Duser%253Aemail"
    user = os.getenv("GITHUB_USERNAME")
    pwd = os.getenv("GITHUB_PWD")

    # Initialize session
    with requests.Session() as s:

        # Github session Login
        r = s.get(login_url)
        soup = BeautifulSoup(r.content, "lxml")

        hidden = soup.find_all("input", {'type':'hidden'})
        target = "https://github.com" + soup.find("form")['action']
        payload = {x["name"]: x["value"] for x in hidden}
        
        # Add login creds to the dict
        payload['login'] = user
        payload['password'] = pwd
        r = s.post(target, data=payload)

        # Start nav to scores page
        cs50_url = 'https://cs50.me'
        r = s.get(cs50_url + '/courses')
        soup = BeautifulSoup(r.content, "lxml")

        # Parse our URL to naviate to scores page
        scores_url= soup.find(name='a', string=re.compile("CS50x 2019"))['href']
        
        # Get branch details from scores page
        r = s.get(cs50_url + scores_url)
        soup = BeautifulSoup(r.content, "html.parser")
        branch_info = list(soup.find_all('a', class_="problem-name"))
        branches = []
        for item in branch_info:
            x = item.string
            x = str(x).strip()
            branches.append(x)

        # Get Submission details from scores page
        submission_info = list(soup.find_all('td', {'data-label':"Submission"}))
        submissions = []
        for item in submission_info:
            x = item.string
            x = str(x).strip()
            submissions.append(x)
        
        # Get Scores details from scores page
        score_info = list(soup.find_all('span', class_="final-score-area"))
        scores = []
        problem = 0

        for item in score_info:
            # Check the tags data-problem field.  If matches previous, skip over
            if item.attrs['data-problem'] == problem:
                continue

            problem = item.attrs['data-problem']    

            # Once validated add score value to list        
            x = item.string
            x = str(x).strip()
            scores.append(x)

        # Go through and add N/A for psets with no score
        for count, val in enumerate(submissions):
            if submissions[count] == 'No Submissions':
                scores.insert(count,'N/A')
        
        
        # Iterate over values and create final grades package
        grades = []
        for count, val in enumerate(branches):
            dct = {
                'branch': branches[count],
                'score': scores[count]
                }

            grades.append(dct)
        
        return grades