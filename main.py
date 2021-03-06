import discord
import subprocess
import requests


from discord.ext import tasks

TOKEN = 'ODQzMTMzOTY5OTM1NzYxNDI4.YJ_bsw.3oOKwHa5E3ciY6s9hM5Dwqm2hgE'
client = discord.Client()
testChannelID = 843136959819808769
twitterStream = None

API_KEY = 'XXRtnvNOBZh0KZw4p32TpWsWO'
API_SECRET = 'ia3NoMRV4hsGXtVBafxsj269T97Uy5v1X6CPkdprjkgguxrIiS'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAK6yPgEAAAAAT1yaXbs9II3eUoVnke7KpmVFKBI' \
               '%3DdU9prVHy1ahBL0ZubzrNHlbTvOP5GLlhZBVXGSEfNy8W9FTXJB'


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	testChannel = client.get_channel(843136959819808769)
	await start_twitter_side()

	check_stream.start()
	# tweet_lookup.start()
	await testChannel.send('We are locked and loaded!')


async def start_twitter_side():
	return subprocess.Popen(['sh', './TwitterSide.sh'],
	                        stdout=subprocess.PIPE,
	                        stdin=subprocess.PIPE)


async def restart_twitter_side():
	subprocess.Popen(['sh', './stop_TwitterSide.sh'],
	                 stdout=subprocess.PIPE,
	                 stdin=subprocess.PIPE
	                 )


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!add'):
		handleList = message.content.split(' ')[1]
		await add_handle_to_stream(handleList.split(','))
	elif message.content.startswith('!help'):
		helpMessage = 'To add a twitter handle to be followed simply say: !add {handle}\n Ex: !add CalebYarnell\n' \
		              'To see all handles being followed currently say: !who'
		await client.get_channel(testChannelID).send(helpMessage)
	elif message.content.startswith('!about'):
		aboutMessage = 'TwitterReadr was developed by Caleb Yarnell for his lovely girlfriend :)\n TwitterReadr streams' \
		               'tweets from user added handles and cross posts it to a discord channel so you never miss the tweets' \
		               'you care about!'
		await client.get_channel(testChannelID).send(aboutMessage)


async def add_handle_to_stream(handles):
	handles_to_add = []
	for name in handles:
		handles_to_add.append({'value': 'from:{}'.format(name.replace(' ', '')), 'tag': 'user_add'})

	req = requests.post('https://api.twitter.com/2/tweets/search/stream/rules',
	                    headers={'Content-type': 'application/json', 'Authorization': 'Bearer {}'.format(BEARER_TOKEN)},
	                    json={'add': handles_to_add})

	if req.status_code != 201:
		await client.get_channel(testChannelID).send('Failed to add some messages :/ GET AN ADMIN!')
		raise Exception(
			"Cannot add rules (HTTP {}): {}".format(
				req.status_code, req.text
			)
		)
	client.get_channel(testChannelID).send('Successfully added all given handles!')


@tasks.loop(seconds=2)
async def check_stream():
	response = requests.get('http://127.0.0.1:5000/tweets')
	if 'status' in response.json():
		return
	tweet_id = response.json()['data']['id']
	await client.get_channel(testChannelID).send(f'https://twitter.com/i/status/{tweet_id}')


async def clear_stream():
	subProcess = subprocess.Popen(['sh', "./clearStream.sh"],
	                              stdout=subprocess.PIPE,
	                              stdin=subprocess.PIPE)


client.run(TOKEN)
