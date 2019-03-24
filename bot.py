# Discord Bot for CS50

import config as cfg
import discord
print(discord.__version__)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        # Intro message whenever bot comes online
        channel = self.get_channel(416576586301702144)
        print(channel)

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
                '- **!stack50 <search term>:** Returns results from the CS50 ' +
                    'Stackexchange \n') 

        # Provide a list of useful links and resources
        if command == '!resources':
            await message.channel.send(
                'The following are some resources you may find helpful ' +
                'during the course of schoolwork and problemsets: ' +
                '- **Discord:** https://discord.gg/QYZQfZ6'
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