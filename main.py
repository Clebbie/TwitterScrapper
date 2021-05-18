import discord
import os
import subprocess
import time
import requests
import json

from discord.ext import tasks

TOKEN = 'ODQzMTMzOTY5OTM1NzYxNDI4.YJ_bsw.3oOKwHa5E3ciY6s9hM5Dwqm2hgE'
client = discord.Client()
testChannelID = 843136959819808769
twitterStream = ''
rawTweetQ = []

API_KEY = 'XXRtnvNOBZh0KZw4p32TpWsWO'
API_SECRET = 'ia3NoMRV4hsGXtVBafxsj269T97Uy5v1X6CPkdprjkgguxrIiS'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAK6yPgEAAAAAT1yaXbs9II3eUoVnke7KpmVFKBI%3DdU9prVHy1ahBL0ZubzrNHlbTvOP5GLlhZBVXGSEfNy8W9FTXJB'


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	testChannel = client.get_channel(843136959819808769)
	twitterStream = subprocess.Popen(['python3', 'TwitterSide.py'],
									 cwd="/home/caleb/PycharmProjects/TwitterScrapper",
									 stdout=subprocess.PIPE,
									 stdin=subprocess.PIPE)

	check_stream.start()
	tweet_lookup.start()
	await testChannel.send('We are locked and loaded!')


@tasks.loop(seconds=2)
async def tweet_lookup():
	if len(rawTweetQ) != 0:
		rawTweet = rawTweetQ.pop()
		headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}
		fields = 'tweet.fields=lang,author_id,text,attachments'
		id = rawTweet['data']['id']
		url = 'https://api.twitter.com/2/tweets?{}&{}'.format(id, fields)

		response = requests.request('GET', url, headers=headers)
		message = response.json()
		await client.get_channel(testChannelID).send(message)


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')


@tasks.loop(seconds=2)
async def check_stream():
	response = requests.get('http://127.0.0.1:5000/tweets')
	if 'status' in response.json():
		return
	rawTweetQ.append(response.json)
	# await client.get_channel(testChannelID).send(response.json())
	print(json.dumps(response.json(), indent=4, sort_keys=True))


async def clear_stream():
	subProcess = subprocess.Popen(['sh', "./clearStream.sh"],
								  stdout=subprocess.PIPE,
								  stdin=subprocess.PIPE)


client.run(TOKEN)
