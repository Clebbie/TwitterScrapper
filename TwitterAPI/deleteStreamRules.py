import json

import requests

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAK6yPgEAAAAAT1yaXbs9II3eUoVnke7KpmVFKBI' \
               '%3DdU9prVHy1ahBL0ZubzrNHlbTvOP5GLlhZBVXGSEfNy8W9FTXJB'


def create_headers():
	headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}
	return headers


headers = create_headers()
rules = ['1415554664725102594','1415554664725102593']

payload = {"delete": {'ids': rules}}
response = requests.post(
	"https://api.twitter.com/2/tweets/search/stream/rules",
	headers=headers,
	json=payload
)
if response.status_code != 200:
	raise Exception(
		"Cannot delete rules (HTTP {}): {}".format(
			response.status_code, response.text
		)
	)
print(json.dumps(response.json()))
