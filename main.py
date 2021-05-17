import discord
import os
import subprocess
import time

from discord.ext import tasks

TOKEN = 'ODQzMTMzOTY5OTM1NzYxNDI4.YJ_bsw.3oOKwHa5E3ciY6s9hM5Dwqm2hgE'
client = discord.Client()
testChannelID = 843136959819808769


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    testChannel = client.get_channel(843136959819808769)
    subProcess = subprocess.Popen(['sh', "python3 TwitterSide.py"],
                                  cwd="/home/PycharmProjects/TwitterScrapper",
                                  stdout=subprocess.PIPE,
                                  stdin=subprocess.PIPE)
    subProcess.wait()
    response = subProcess.stdout.readlines()
    print(response)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@tasks.loop(seconds=10)
async def check_stream():
    subProcess = subprocess.Popen(['sh', "python3 TwitterSide.py"],
                                  cwd="/home/PycharmProjects/TwitterScraper",
                                  stdout=subprocess.PIPE,
                                  stdin=subprocess.PIPE)
    subProcess.wait()
    response = subProcess.stdout.readlines()


    response = [line.decode('utf-8') for line in response]
    print(response)
    await client.get_channel(testChannelID).send(response)

async def clear_stream():
    subProcess = subprocess.Popen(['sh', "./clearStream.sh"],
                                  stdout=subprocess.PIPE,
                                  stdin=subprocess.PIPE)

client.run(TOKEN)
