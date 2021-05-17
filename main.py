import discord
import os
import subprocess
import time

TOKEN = 'ODQzMTMzOTY5OTM1NzYxNDI4.YJ_bsw.3oOKwHa5E3ciY6s9hM5Dwqm2hgE'
client = discord.Client()
testChannelID = 843136959819808769


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    testChannel = client.get_channel(843136959819808769)

    # twitterStream = subprocess.Popen(['sh', './TwitterSide.sh'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    # twitterStream.wait()
    # open("streamBuffer.txt","r")
    # response = twitterStream.stdout.readlines()
    # print(response)
    while True:
        await check_stream()
        await time.sleep(5)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


async def check_stream():
    subProcess = subprocess.Popen(['sh', "./readStream.sh"],
                                  stdout=subprocess.PIPE,
                                  stdin=subprocess.PIPE)
    subProcess.wait()
    response = subProcess.stdout.readlines()


    response = [line.decode('utf-8') for line in response]
    print(response)
    await client.get_channel(testChannelID).send(response)


client.run(TOKEN)
