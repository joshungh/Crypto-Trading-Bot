import datetime
import hashlib
import hmac
import requests
import time
from decimal import Decimal

_API_URL = 'https://www.bitstamp.net/api/'

def dt(timestamp):
    """
    Convert a unix timestamp or ISO 8601 date string to a datetime object.
    """
    if not timestamp:
        return None
    try:
        timestamp = int(timestamp)
    except ValueError:
        try:
            timestamp = time.mktime(
                time.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f'))
        except ValueError:
            timestamp = time.mktime(
                time.strptime(timestamp, '%Y-%m-%d %H:%M:%S'))
    return datetime.datetime.fromtimestamp(timestamp)


class APIError(Exception):
    pass


class APICall(object):
    url = None
    method = 'get'

    def _process_response(self, response):
        """
        Process the response dictionary.
        If the dictionary is just being altered, then no return is necessary.
        Alternatively, a totally different response can be returned.
        """
        return

    def call(self, **params):
        # Form request
        r = None
        url = _API_URL + self.url
        if self.method == 'get':
            r = requests.get(url, params=params)
        elif self.method == 'post':
            r = requests.post(url, data=params)
        response = r.json()
        # API error?
        if isinstance(response, dict) and 'error' in response:
            raise APIError(response['error'])
        # Process fields
        new_response = self._process_response(response)
        if new_response is not None:
            response = new_response
        return response

print response

class APIPrivateCall(APICall):
    method = 'post'

    def __init__(self, client_id, api_key, api_secret, *args, **kwargs):
        super(APIPrivateCall, self).__init__(*args, **kwargs)
        self.client_id = 'xxx'
        self.api_key = 'xxx'
        self.api_secret = 'xxx'

    def _get_nonce(self):
        return str(int(time.time() * 1e6))

    def call(self, **params):
        nonce = self._get_nonce()
        message = nonce + self.client_id + self.api_key
        signature = hmac.new(
            self.api_secret, msg=message, digestmod=hashlib.sha256)
        signature = signature.hexdigest().upper()
        params.update({
            'key': self.api_key, 'signature': signature, 'nonce': nonce
        })
        return super(APIPrivateCall, self).call(**params)
