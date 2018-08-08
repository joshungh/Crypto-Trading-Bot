import bitstamp.client
import time, json, requests
import arrow
import gdax
from geminipy import Geminipy


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Price tracking code

print "TwinBot 1.2 == Gemini & GDAX Arbitrage Trading Bot"
print "updated 8/28/2017 == xxx"
print "Start Time:", arrow.now()

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


gemini_BID = float(geminiBID())
gemini_ASK = float(geminiASK())
GDAX_BID = float(GDAXBID())
GDAX_ASK = float(GDAXASK())

R4 = float(((gemini_BID/GDAX_ASK)*100)-100.5)
R6 = float(((GDAX_ASK/gemini_BID)*100)-100.5)

# GDAX

auth_client = gdax.AuthenticatedClient('5840df6215732d78d8ee5cd30dc4d447', 'D55kFQKyW/uo86au78dB1JZrgoJmYyy7s10+spKHE5bUsR0KRhz934bSrHxKs+lWiTwcrD3sM+CjXD5hKX147w==', '!a3sdf54ga3sd@#sda@5')

gdax_buy_price = (float(GDAXASK()))
gdax_sell_price = (float(GDAXBID()))

def gdax_buy_order():
	auth_client.buy(price=gdax_buy_price,
					size=0.01,
					product_id='ETH-BTC')

def gdax_sell_order():
	auth_client.sell(price=gdax_sell_price,
					size=0.01,
					product_id='ETH-BTC')

#GEMINI

con = Geminipy(api_key='ivrwpKOnNKTNCcLNvvwV', secret_key='Ti3rdGhuTcXsYQPxGixCgTdw4z2', live=True)

gem_buy_price = (float(geminiASK()))
gem_sell_price = (float(geminiBID()))

def gem_buy_order():
	order = con.new_order(amount=0.01, price=gem_buy_price, side='buy')

def gem_sell_order():
	order = con.new_order(amount=0.01, price=gem_sell_price, side='sell')

while True:
	if R6>0.05:
		gdax_sell_order()
		gem_buy_order()
		print ("TRADE MADE!", arrow.now())

	elif R4>0.05:
		gdax_buy_order()
		gem_sell_order()
		print ("TRADE MADE!", arrow.now())

	else:
		print "...scanning trade conditions..."

	time.sleep(0.2)
