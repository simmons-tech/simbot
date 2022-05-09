import os

import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    cont = message.content.lower()
    if 'where' in cont and ('rapid' in cont or 'antigen' in cont) and 'test' in cont:
        await message.reply(('The rapid antigen tests are in Kristen\'s office'
                             ' in the mailbox lounge! The door should be unloc'
                             'ked, so you can get them whenever you need them.'))

client.run(os.environ['DISCORD_TOKEN'])
