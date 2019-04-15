```
   ____  ____  ____    ___          ____    ___  _____ 
  / ___|/ ___|| ___|  / _ \        | __ )  / _ \|_   _|
 | |    \___ \|___ \ | | | | _____ |  _ \ | | | | | |  
 | |___  ___) |___) || |_| ||_____|| |_) || |_| | | |  
  \____||____/|____/  \___/        |____/  \___/  |_|
```
 ====================================================

CS50-Bot is a discord bot designed to serve as a personal helper for online 
students of Harvard's CS50 course.  For simplicity, the bot is designed to be run locally on a 
student's machine although it can be hosted anywhere.  The intention is for the bot to be run in a user's private personal discord as some of the commands are tied to a single users.

Besides providing helpful commannds and resournces, it also serves the practical purpose of showing students how to set up and run their own application.  I've tried to make it functional without requiring new students to do anything too complicated like setting up a database.

# Getting Started
You should sign up for a Github account if you have not already.  If you are a new student, you will need one for CS50.  This writeup also assumes are familiar with Discord and know how to create your own discord server if you don't have one already. 

1) Download this Github repository and save it on your local machine.
2) Download and install [Python 3.7](https://www.python.org/downloads/release/python-370/) onto the machine you will use to run the bot.

# Creating a Bot Account
Next you will will want to register a bot account with discord.  There are many online tutorials, but I find this one to be an easy step by step guide (https://discordpy.readthedocs.io/en/rewrite/discord.html).

Once you have your bot set up, make sure you copy your token somewhere safe as you will need it to set your config file.  Do not share or expose your token.

# Setting Up config.py file
The last step will be to manualy setup a config file.  This file saves all your private settings that the bot will need such as usernames, passwords, bot token etc.  Make sure you do not expose these publically (such as an online repository).

1) Open a new file in a text editor of your choice
2) Paste the following code

    ```python
    # Config file for CS50 Bot

    discord = {
        'token' : 'YOUR_TOKEN_HERE' 
    }

    github = {
        'username' : 'GITHUB_USERNAME_HERE',
        'password' : 'GITHUB_PASSWORD_HERE'
    }
    ```
3) Replace the placeholder values (ex: 'YOUR_TOKEN_HERE') with the correct ones for your application.  Make sure to put the inbetween the quote marks.
4) Save the file in the root directory of the folder you saved earlier.  This is the same location where the bot.py file is located.

# Starting Your Bot
Now that everything has been installed, you are ready to start running CS50-Bot.  Navigate to the folder containing the bot.py file and double click.  You should see the python shell running and your discord bot in your server.

Alternatively you can run it from the command line by navigating to the appropriate location and typing:
`python bot.py`

In discord type "!help" to see a list of all available commands.