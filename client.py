import requests
import json
from decimal import Decimal
import os

URL = os.environ.get('XSTARZ_MARKETSCAN_URL')
ACCOUNT = os.environ.get('XSTARZ_MARKETSCAN_ACCOUNT')

def cast(d):
    for k, v in d.items():
        if isinstance(v, dict):
            cast(v)
        elif isinstance(v, Decimal):
            d[k] = float(v)

class Client():
    def __init__(self, action, url=URL, account=ACCOUNT):
        self._url = url
        self.account = account
        self.action = action

    @property
    def url(self):
        return '{}{}{}'.format(self._url, self.action, self.account)
    
    @property
    def requests(self):
        return requests

    def post(self, json_string):
        response = self.requests.post(self.url, json=json.loads(json_string.strip()))
        try:
            return json.dumps(response.json(), indent=2, sort_keys=True)
        except:
            return response.content
            

    def get(self):
        response = self.requests.get(self.url)
        try:
            return json.dumps(response.json(), indent=2, sort_keys=True)
        except:
            return response.content

    @staticmethod
    def from_json(data):
        return json.loads(data)

    @staticmethod
    def to_json(data):
        try:
            return json.dumps(data)
        except:
            cast(data)
            return json.dumps(data)


