import discord
import os
import subprocess
import time
import requests

from discord.ext import tasks

TOKEN = 'ODQzMTMzOTY5OTM1NzYxNDI4.YJ_bsw.3oOKwHa5E3ciY6s9hM5Dwqm2hgE'
client = discord.Client()
testChannelID = 843136959819808769
twitterStream = ''


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    testChannel = client.get_channel(843136959819808769)
    twitterStream = subprocess.Popen(['python3', 'TwitterSide.py'],
                                     cwd="/home/caleb/PycharmProjects/TwitterScrapper",
                                     stdout=subprocess.PIPE,
                                     stdin=subprocess.PIPE)

    await testChannel.send('We are locked and loaded!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@tasks.loop(seconds=2)
async def check_stream():
    response = requests.get('http://127.0.0.1:5000')
    if 'status' in response.json():
        return
    await client.get_channel(testChannelID).send(response.json())


async def clear_stream():
    subProcess = subprocess.Popen(['sh', "./clearStream.sh"],
                                  stdout=subprocess.PIPE,
                                  stdin=subprocess.PIPE)


client.run(TOKEN)
