import requests
import json

example = {}
example['data'] = {'id': '1394702409528655874', 'text': 'Testy'}
example['matching_rules'] = [{'id': 1415554664725102594, 'tag': 'gamer'}]
myserver = 'http://127.0.0.1/5000'
body = json.dumps(example, indent=4, sort_keys=True)
requests.post(myserver, body, example)
