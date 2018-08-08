#Live Bitcoin Price Tracker v1.0
#Bitstamp, Bitfinex, GDAX, Gemini, Poloniex
import time, json, requests
import arrow


print "--------------------------------------------------"
print "BITCOIN PRICE TRACKER v1.1"
print "Definition of Ratios:"
print "R1 = % spread between Bitstamp/Gemini"
print "R2 = % spread between Bitstamp/GDAX"
print "R3 = % spread between Gemini/GDAX"
print "--------------------------------------------------"

def bitstamp():
	bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
	return bitStampTick.json()['last'] #'last' returns most recent BTC:USD price
	
def gemini():
	geminiTick = requests.get('https://api.gemini.com/v1/pubticker/btcusd')
	return geminiTick.json() ['last']
	
def GDAX():
	GDAXTick = requests.get('https://api.gdax.com/products/BTC-USD/ticker')
	return GDAXTick.json() ['price']
	
	
while True:
	bitstamp_USD = float(bitstamp())
	gemini_USD = float(gemini())
	GDAX_USD = float(GDAX())
	
	R1 = float(100-((bitstamp_USD/gemini_USD)*100))
	R2 = float(100-((bitstamp_USD/GDAX_USD)*100))
	R3 = float(100-((gemini_USD/GDAX_USD)*100))
	
	print
	print "Time:", arrow.now()
	print "Bitstamp:", bitstamp_USD
	print "Gemini:  ", gemini_USD
	print "GDAX:    ", GDAX_USD
	print "...................................."
	print "R1, % spread:", "%.4f" % R1
	print "R2, % spread:", "%.4f" % R2
	print "R3, % spread:", "%.4f" % R3
	print
	print "======================================"

	time.sleep(2)
	
	
	