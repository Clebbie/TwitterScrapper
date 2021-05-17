import discord
import os
import subprocess
import time

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
    twitterStream.wait()
    response = twitterStream.stdout.readlines()
    print(response)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@tasks.loop(seconds=5)
async def check_stream():
    response = twitterStream.stdout.readlines()
    await client.get_channel(testChannelID).send(response)


async def clear_stream():
    subProcess = subprocess.Popen(['sh', "./clearStream.sh"],
                                  stdout=subprocess.PIPE,
                                  stdin=subprocess.PIPE)


client.run(TOKEN)
