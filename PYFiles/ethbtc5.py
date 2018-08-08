#Live Bitcoin:Ether Price Tracker v1.0
#Bitstamp, Bitfinex, GDAX, Gemini, Poloniex
import time, json, requests
import arrow


print "--------------------------------------------------"
print "BITCOIN PRICE TRACKER v1.2"
print "Definition of Ratios:"
print "R1 = % spread between Bitstamp(ASK)/Gemini(BID)"
print "R2 = % spread between Bitstamp(ASK)/GDAX(BID)"
print "R3 = % spread between Gemini(ASK)/Bitstamp(BID)"
print "R4 = % spread between Gemini(ASK)/GDAX(BID)"
print "R5 = % spread between GDAX(ASK)/Bitstamp(BID)"
print "R6 = % spread between GDAX(ASK)/Gemini(BID)"
print "--------------------------------------------------"

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

	
print "Start Time:", arrow.now()

while True:
	bitstamp_BID = float(bitstampBID())
	bitstamp_ASK = float(bitstampASK())
	gemini_BID = float(geminiBID())
	gemini_ASK = float(geminiASK())
	GDAX_BID = float(GDAXBID())
	GDAX_ASK = float(GDAXASK())
	
	R1 = float(((bitstamp_ASK/gemini_BID)*100)-100.5)
	R2 = float(((bitstamp_ASK/GDAX_BID)*100)-100.5)
	R3 = float(((gemini_ASK/bitstamp_BID)*100)-100.5)
	R4 = float(((gemini_ASK/GDAX_BID)*100)-100.5)
	R5 = float(((GDAX_ASK/bitstamp_BID)*100)-100.5)
	R6 = float(((GDAX_ASK/gemini_BID)*100)-100.5)
	print R4
	print R6
	
	if R1>0.1:
		print "R1 (Time --- Spread):", arrow.now(), "---", "%.4f" % R1
	if R2>0.1:
		print "R2 (Time --- Spread):", arrow.now(), "---", "%.4f" % R2
	if R3>0.1:
		print "R3 (Time --- Spread):", arrow.now(), "---", "%.4f" % R3
	if R4>0.1:
		print "R4 (Time --- Spread):", arrow.now(), "---", "%.4f" % R4
	if R5>0.1:
		print "R5 (Time --- Spread):", arrow.now(), "---", "%.4f" % R5
	if R6>0.1:
		print "R6 (Time --- Spread):", arrow.now(), "---", "%.4f" % R6

	time.sleep(0.2)