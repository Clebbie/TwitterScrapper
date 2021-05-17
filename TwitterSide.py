import requests
import os
import json

API_KEY = 'XXRtnvNOBZh0KZw4p32TpWsWO'
API_SECRET = 'ia3NoMRV4hsGXtVBafxsj269T97Uy5v1X6CPkdprjkgguxrIiS'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAK6yPgEAAAAAT1yaXbs9II3eUoVnke7KpmVFKBI%3DdU9prVHy1ahBL0ZubzrNHlbTvOP5GLlhZBVXGSEfNy8W9FTXJB'

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def get_rules(headers, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(headers, bearer_token, rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
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


def set_rules(headers, delete, bearer_token):
    # You can adjust the rules if needed
    sample_rules = [
        {"value": "from:BTS_twt", "tag": "bts"},
        {"value": "from:theOnlyYarnBall", "tag": "gamer"},
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(headers, set, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    # bufferFile = open("streamBuffer.txt", "a+")
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            # bufferFile.write("hahahahahahahahah this works!")
            # bufferFile.write(json.dumps(json_response, indent=4, sort_keys=True))
            print(json.dumps(json_response, indent=4, sort_keys=True))


def main():
    bearer_token = BEARER_TOKEN
    headers = create_headers(bearer_token)
    rules = get_rules(headers, bearer_token)
    delete = delete_all_rules(headers, bearer_token, rules)
    my_set = set_rules(headers, delete, bearer_token)
    get_stream(headers, my_set, bearer_token)

main()



