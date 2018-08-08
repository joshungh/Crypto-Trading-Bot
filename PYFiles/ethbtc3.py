#Live Bitcoin:Ether Price Tracker v1.0
#Bitstamp, Bitfinex, GDAX, Gemini, Poloniex
import time, json, requests
import arrow


print "--------------------------------------------------"
print "BITCOIN PRICE TRACKER v1.2* Gemini down for maintenance & therefore omitted"
print "Definition of Ratios:"
print "R2 = % spread between Bitstamp(ASK)/GDAX(BID)"
print "R5 = % spread between GDAX(ASK)/Bitstamp(BID)"
print "--------------------------------------------------"

def bitstampBID():
	bitStampTick = requests.get('https://www.bitstamp.net/api/v2/ticker/ethbtc/')
	return bitStampTick.json()['bid'] #'bid' returns most best bid to buy offer
	
def bitstampASK():
	bitStampTick = requests.get('https://www.bitstamp.net/api/v2/ticker/ethbtc/')
	return bitStampTick.json()['ask'] #'ask' returns most best ask to sell offer

def GDAXBID():
	GDAXTick = requests.get('https://api.gdax.com/products/ETH-BTC/ticker')
	return GDAXTick.json() ['bid']
	
def GDAXASK():
	GDAXTick = requests.get('https://api.gdax.com/products/ETH-BTC/ticker')
	return GDAXTick.json() ['ask']

	
print "Start Time:", arrow.now()

while True:
	bitstamp_BID = float(bitstampBID())
	bitstamp_ASK = float(bitstampASK())
	GDAX_BID = float(GDAXBID())
	GDAX_ASK = float(GDAXASK())
	
	R2 = float(((bitstamp_ASK/GDAX_BID)*100)-100.5)
	R5 = float(((GDAX_ASK/bitstamp_BID)*100)-100.5)
	
	if R2>0.1:
		print "R2 (Time --- Spread):", arrow.now(), "---", "%.4f" % R2
	if R5>0.1:
		print "R5 (Time --- Spread):", arrow.now(), "---", "%.4f" % R5

	time.sleep(0.2)