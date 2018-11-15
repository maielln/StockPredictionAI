import requests
import json

# Standard http GET request
def get (url):
    res = requests.get(url)
    try:
        res = json.loads(res.content)
    except json.decoder.JSONDecodeError:
        print('Error converting json')
        print('Input Data:')
        print(res)
    return res