import requests
import json

PROTOCOL='http'
HOST='localhost'
PORT=8000

def get(self, enpoint: str):
    self.response = requests.get(self.url)
    self.print_response()

def post(self, enpoint: str, payload):
    url = f"{PROTOCOL}://{HOST}:{PORT}{endpoint}"
    self.response = requests.post(self.url, json=payload)
    self.print_response()

def put(enpoint: str, payload):
    # if(endpoint[:1]!='/'):
    #     endpoint='/'+enpoint
    url = f"{PROTOCOL}://{HOST}:{PORT}{endpoint}"
    return requests.put(url, json=payload)

def print_response(response: requests.Response):
    print(response.status_code, response.headers['content-type'])
    if response.headers['content-type'] == 'application/json' or response.headers['content-type'] == 'application/json; charset=utf-8':
        print(json.dumps(json.loads(response.content), indent=4))


print_response(get(''))

endpoint = '/items/1'
print_response(get(endpoint))

endpoint = '/items/1'
print_response(post(endpoint))

endpoint = '/items/1'
payload = {
    "name": "string",
    "price": 0,
    "is_offer": True
}
print_response(put(endpoint, payload))
