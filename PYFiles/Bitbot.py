import hmac
import hashlib
import requests
import time
import json

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

##requests.post('https://www.bitstamp.net/api/v2/buy/ethbtc', data='postCall')

def buyTick():
	auth_client = requests.post(url, data=json.dumps(payload))

def report():
	reportx = requests.get(url)
	return reportx.json() [usd_balance]


def BTCbalance():
	balance = requests.get(url)
	return balance.json()[xrp_available]

balance_usd = float(report())

print balance_usd
