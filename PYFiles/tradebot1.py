#Trading Bot v1.0
import time, json, requests
import hmac
import httplib
import urllib
import hashlib
import hmac

#bitstamp public key: L8OLdTCVcVrafH2brfDtfibVtlbIW9w0
#bitstamp private key: OVi4JQiOjZjnQ8ipjrzizYXKxVICdHLz
#gemini public key: ivrwpKOnNKTNCcLNvvwV
#gemini private key: Ti3rdGhuTcXsYQPxGixCgTdw4z2
#GDAX public key: 5840df6215732d78d8ee5cd30dc4d447
#GDAX private key: D55kFQKyW/uo86au78dB1JZrgoJmYyy7s10+spKHE5bUsR0KRhz934bSrHxKs+lWiTwcrD3sM+CjXD5hKX147w==
#GDAX passphrase: !a3sdf54ga3sd@#sda@5

bitstamp_api_key = 'L8OLdTCVcVrafH2brfDtfibVtlbIW9w0'
bitstamp_secret_key = 'OVi4JQiOjZjnQ8ipjrzizYXKxVICdHLz'
gemini_api_key = 'ivrwpKOnNKTNCcLNvvwV'
gemini_secret_key = 'Ti3rdGhuTcXsYQPxGixCgTdw4z2'
gdax_api_key = '5840df6215732d78d8ee5cd30dc4d447'
gdax_private_key = 'D55kFQKyW/uo86au78dB1JZrgoJmYyy7s10+spKHE5bUsR0KRhz934bSrHxKs+lWiTwcrD3sM+CjXD5hKX147w=='

def bitstamptrade_buy(txRate,qty):
	nonce = int(round(time.time()-1502951600,1)*10)

	message = 'nonce' + '922244' + 'bitstamp_api_key'
	
	signature = hmac.new(
		bitstamp_secret_key,
		msg=message,
		digestmod=hashlib.sha256
	).hexdigest().upper()
	
	parms = {"key":bitstamp_api_key,
			 "signature":signature,
			 "nonce":nonce,
			 "amount":qty,
			 "price":txRate}
	
	headers = {"Content-type":"application/x-www-form-urlencoded",
			   "Key":bitstamp_api_key,
			   "signature":signature}
	
	conn = httplib.HTTPSConnection("//bitstamp.net/api/v2/buy/btcusd/")
	conn.request("POST", parms, message, headers)

bitstamptrade_buy(4500,0.01)
