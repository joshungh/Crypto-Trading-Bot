#Live Bitcoin Price Tracker v1.0
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
	bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
	return bitStampTick.json()['bid'] #'bid' returns most best bid to buy offer
	
def bitstampASK():
	bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
	return bitStampTick.json()['ask'] #'ask' returns most best ask to sell offer
	
def geminiBID():
	geminiTick = requests.get('https://api.gemini.com/v1/pubticker/btcusd')
	return geminiTick.json() ['bid']

def geminiASK():
	geminiTick = requests.get('https://api.gemini.com/v1/pubticker/btcusd')
	return geminiTick.json() ['ask']
	
def GDAXBID():
	GDAXTick = requests.get('https://api.gdax.com/products/BTC-USD/ticker')
	return GDAXTick.json() ['bid']
	
def GDAXASK():
	GDAXTick = requests.get('https://api.gdax.com/products/BTC-USD/ticker')
	return GDAXTick.json() ['ask']
	
while True:
	bitstamp_BID = float(bitstampBID())
	bitstamp_ASK = float(bitstampASK())
	gemini_BID = float(geminiBID())
	gemini_ASK = float(geminiASK())
	GDAX_BID = float(GDAXBID())
	GDAX_ASK = float(GDAXASK())
	
	R1 = float((bitstamp_ASK/gemini_BID)*100)-100
	R2 = float((bitstamp_ASK/GDAX_BID)*100)-100
	R3 = float((gemini_ASK/bitstamp_BID)*100)-100
	R4 = float((gemini_ASK/GDAX_BID)*100)-100
	R5 = float((GDAX_ASK/bitstamp_BID)*100)-100
	R6 = float((GDAX_ASK/gemini_BID)*100)-100
	print
	print "Time:", arrow.now()
	print
	print "Bitstamp, Ask:", bitstamp_ASK
	print "Bitstamp, Bid:", bitstamp_BID
	print "Gemini, Ask:  ", gemini_ASK
	print "Gemini, Bid:  ", gemini_BID
	print "GDAX, Ask:    ", GDAX_ASK
	print "GDAX, Bid:    ", GDAX_BID
	print "...................................."
	print "R1, % spread:", "%.4f" % R1
	print "R2, % spread:", "%.4f" % R2
	print "R3, % spread:", "%.4f" % R3
	print "R4, % spread:", "%.4f" % R4
	print "R5, % spread:", "%.4f" % R5
	print "R6, % spread:", "%.4f" % R6	
	print
	print "======================================"

	time.sleep(3)