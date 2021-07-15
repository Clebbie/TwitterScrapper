import json

import requests

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAK6yPgEAAAAAT1yaXbs9II3eUoVnke7KpmVFKBI' \
               '%3DdU9prVHy1ahBL0ZubzrNHlbTvOP5GLlhZBVXGSEfNy8W9FTXJB'
url = 'https://api.twitter.com/2/tweets/search/stream/rules'
headers = {'Authorization': 'Bearer {}'.format(BEARER_TOKEN)}
req = requests.get(url=url, headers=headers)

print(json.dumps(req.json()))
