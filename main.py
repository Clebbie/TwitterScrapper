import discord
import os
import subprocess

TOKEN = 'ODQzMTMzOTY5OTM1NzYxNDI4.YJ_bsw.3oOKwHa5E3ciY6s9hM5Dwqm2hgE'
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    twitterStream = await subprocess.Popen(['sh', 'TwitterSide.sh'], cwd='/home/PycharmProjects/TwitterScrapper/', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    await twitterStream.wait()
    response = await twitterStream.stdout.readlines()
    print(response)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(TOKEN)
