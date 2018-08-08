#Live Bitcoin:Ether Price Tracker v1.0
#Bitstamp, Bitfinex, GDAX, Gemini, Poloniex
import time, json, requests
import arrow
import gdax

#Request for exchange bid/ask prices for ETH in BTC/ETH

def bitstampBID():
	bitStampTick = requests.get('https://www.bitstamp.net/api/v2/ticker/ethbtc/')
	return bitStampTick.json()['bid'] #'bid' returns most best bid to buy offer
	
def bitstampASK():
	bitStampTick = requests.get('https://www.bitstamp.net/api/v2/ticker/ethbtc/')
	return bitStampTick.json()['ask'] #'ask' returns most best ask to sell offer
	
def geminiBID():
	geminiTick = requests.get('https://api.gemini.com/v1/pubticker/ethbtc')
	return geminiTick.json() ['bid']

def geminiASK():
	geminiTick = requests.get('https://api.gemini.com/v1/pubticker/ethbtc')
	return geminiTick.json() ['ask']
	
def GDAXBID():
	GDAXTick = requests.get('https://api.gdax.com/products/ETH-BTC/ticker')
	return GDAXTick.json() ['bid']
	
def GDAXASK():
	GDAXTick = requests.get('https://api.gdax.com/products/ETH-BTC/ticker')
	return GDAXTick.json() ['ask']

auth_client = gdax.AuthenticatedClient('5840df6215732d78d8ee5cd30dc4d447', 'D55kFQKyW/uo86au78dB1JZrgoJmYyy7s10+spKHE5bUsR0KRhz934bSrHxKs+lWiTwcrD3sM+CjXD5hKX147w==', '!a3sdf54ga3sd@#sda@5')
	

while True:
	bitstamp_BID = float(bitstampBID())
	bitstamp_ASK = float(bitstampASK())
	gemini_BID = float(geminiBID())
	gemini_ASK = float(geminiASK())
	GDAX_BID = float(GDAXBID())
	GDAX_ASK = float(GDAXASK())

	auth_client.sell(price='x',
					size='0.01',
					product_id='ETH-BTC')
					
	time.sleep(0.5)

