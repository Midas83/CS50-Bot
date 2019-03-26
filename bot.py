# Discord Bot for CS50

import config as cfg
import discord
print(discord.__version__)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        # Intro message whenever bot comes online
        channel = self.get_channel(416576586301702144)
        
        await channel.send('CS50-Bot is online!.  I\'m here to here ' +
                              'to help with all your needs while progressing' +
                              ' through Harvard\'s online CS50 course.  Type ' +
                              '\"!help\" to learn more about me.')
    
    async def on_message(self, message):
        command = message.content.split()[0]
        content = message.content.split()
        del content[0]

        # Don't respond to ourselves
        if message.author == self.user:
            return
        
        # Simple test command
        if command == '!ping':
            await message.channel.send('pong')

        # Help command
        if command == '!help':
            await message.channel.send(
                'Here are a list of commands: \n \n' + 
                '- **!help:**  List of all available commands \n' + 
                '- **!resources:** Returns a list of helpful resources \n' +
                '- **!stack50 <search term>:** Returns results from the CS50 ' +
                    'Stackexchange \n') 

        # Provide a list of useful links and resources
        if command == '!resources':
            await message.channel.send(
                'Nothing beats Google but here are some resources you may' +
                'find helpful for schoolwork and problemsets: \n \n' +
                '__**CS50 SPECIFIC RESOURCES**__ \n' +
                '- **CS50 Discord:** <https://discord.gg/QYZQfZ6> \n' +
                '- **CS50 Reddit:** <http://www.reddit.com/r/cs50> \n'+
                '- **CS50 StackEchange:** <http://cs50.stackexchange.com/> \n' +
                '- **CS50 Reference Doc:** <https://reference.cs50.net/> \n' +
                '- **CS50 IDE**: <https://cs50.io/> \n' +
                '- **CS50 Sandbox**: <https://sandbox.cs50.io/> \n' +
                '- **CS50.me (Grades)**: <https://cs50.me/> \n' +
                '- **CS50 Github**: <https://github.com/cs50> \n \n' +

                '__**OTHER DEV RESOURCES**__ \n' +
                '- **StackOverflow**: <https://stackoverflow.com/> Other ' +
                'than Google, probably the most useful site for solving ' +
                'programming issues \n' +
                '- **W3 Schools**: <https://www.w3schools.com/> Tutorials' +
                'for everything from HTML to Javascript to Python and more \n' +
                '- **Bootstrap**: <https://getbootstrap.com/> Popular library ' +
                'for developing with HTML, CSS and Javascript \n' +
                '- **Notepad++**: <https://notepad-plus-plus.org/> Simple, ' +
                'free, open source code editor \n' +
                '- **VS Code**: <https://code.visualstudio.com/> More robust ' +
                'code editor. Preferred by many developers'
            )

        # Search cs50 stack exchange
        if command == "!stack50":
            print(content)
            # Make sure user provided a search string
            if content == False:
                await message.channel.send('Please provide a search term')
            
            query = "+"
            query = query.join(content)

            await message.channel.send('https://cs50.stackexchange.com/search' +
            '?q=' + query)
            
client = MyClient()
client.run(cfg.discord['token'])