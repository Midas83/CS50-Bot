# Discord Bot for CS50

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!ping':
            await message.channel.send('pong')

        # Search cs50 stack exchange
        if message.content == '!stack':
            print(message)

client = MyClient()
client.run('NTU4MzMyNzQyNjEwMzIxNDA4.D3VTvA.0A4yDcW9cPFExPb1Oq3b4pu4aSs')