#Live Bitcoin Price Tracker v1.0
#Bitstamp, Bitfinex, GDAX, Gemini, Poloniex
import time, json, requests

#I used the public APIs, but we'll be using private APIs for sending orders
def bitstamp():
	bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
	return bitStampTick.json()['last'] #'last' returns most recent BTC:USD price
	
def gemini():
	geminiTick = requests.get('https://api.gemini.com/v1/pubticker/btcusd')
	return geminiTick.json() ['last']

	
while True:
	bitstampUSDLive = float(bitstamp())
	geminiUSDLive = float(gemini())
	
	R1 = float(bitstampUSDLive/geminiUSDLive) #ratio of prices to be used to determine when to buy/sell
	
	print
	print "********************************"
	print "**LAST PRICE OF BITCOIN IN USD**"
	print "********************************"
	print
	print "Bitstamp, USD:", bitstampUSDLive
	print "Gemini, USD:", geminiUSDLive
	print "...................................."
	print "Ratio of Bitstamp over Gemini:", R1
	print; print "=================================================================================="

	time.sleep(2) #enter number of seconds, NOT TO BE LESS THAN 0.2.
	
	
	