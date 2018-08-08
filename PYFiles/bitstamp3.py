import json
import requests
import time
import hmac
import hashlib
import urllib
import httplib


url = 'https://www.bitstamp.net/api/balance/'
headers = {'content-type': 'application/json'}
nonce = int(round(time.time()-1502951600,1)*10)
customer_id = 922244
api_key = 'L8OLdTCVcVrafH2brfDtfibVtlbIW9w0'
API_SECRET = 'xxx'

message = 'nonce' + 'customer_id' + 'api_key'
signature = hmac.new(
	API_SECRET,
	msg=message,
	digestmod=hashlib.sha256
).hexdigest().upper()

payload = {
	'api_key': 'api_key',
	'signature': 'signature',
	'nonce': 'nonce'
}

request = requests.post(url, data=json.dumps(payload), headers=headers)

def BTCbalance():
	balance = requests.get(url)
	return balance.json()['xrp_available']

print BTCbalance()
