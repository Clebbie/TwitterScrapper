import json
import sys

import requests


url = 'https://api.twitter.com/2/users/{}'.format(sys.argv[1])
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAK6yPgEAAAAAT1yaXbs9II3eUoVnke7KpmVFKBI' \
               '%3DdU9prVHy1ahBL0ZubzrNHlbTvOP5GLlhZBVXGSEfNy8W9FTXJB'
headers = {'Authorization': 'Bearer {}'.format(BEARER_TOKEN)}
response = requests.get(url=url,headers=headers)

print(json.dumps(response.json()))