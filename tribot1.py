import bitstamp.client
import time, json, requests
import arrow
import gdax
from geminipy import Geminipy

#Price tracking code +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print "TwinBot 1.2 == Gemini & GDAX Arbitrage Trading Bot"
print "updated 8/28/2017 == christophercoca@gmail.com"
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
	
def bitstampBID():
	bitStampTick = requests.get('https://www.bitstamp.net/api/v2/ticker/ethbtc/')
	return bitStampTick.json()['bid'] #'bid' returns most best bid to buy offer
	
def bitstampASK():
	bitStampTick = requests.get('https://www.bitstamp.net/api/v2/ticker/ethbtc/')
	return bitStampTick.json()['ask'] #'ask' returns most best ask to sell offer
	
bitstamp_BID = float(bitstampBID())
bitstamp_ASK = float(bitstampASK())
gemini_BID = float(geminiBID())
gemini_ASK = float(geminiASK())
GDAX_BID = float(GDAXBID())
GDAX_ASK = float(GDAXASK())

R1 = float(((bitstamp_BID/gemini_ASK)*100)-100.5)
R2 = float(((bitstamp_BID/GDAX_ASK)*100)-100.5)
R3 = float(((gemini_BID/bitstamp_ASK)*100)-100.5)
R4 = float(((gemini_BID/GDAX_ASK)*100)-100.5)
R5 = float(((GDAX_BID/bitstamp_ASK)*100)-100.5)
R6 = float(((GDAX_BID/gemini_ASK)*100)-100.5)

# GDAX +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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


#GEMINI ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

con = Geminipy(api_key='ivrwpKOnNKTNCcLNvvwV', secret_key='Ti3rdGhuTcXsYQPxGixCgTdw4z2', live=True)

gem_buy_price = (float(geminiASK()))
gem_sell_price = (float(geminiBID()))

def gem_buy_order():
	order = con.new_order(amount=0.01, price=gem_buy_price, side='buy')
	
def gem_sell_order():
	order = con.new_order(amount=0.01, price=gem_sell_price, side='sell')
	
# Bitstamp ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
	
bit_public_client = bitstamp.client.Public()

bit_trading_client = bitstamp.client.Trading(
	username='922244', key='L8OLdTCVcVrafH2brfDtfibVtlbIW9w0', secret='OVi4JQiOjZjnQ8ipjrzizYXKxVICdHLz')

bit_bid = bit_public_client.ticker()['bid']
bit_ask = bit_public_client.ticker()['ask']
min_amount_1 = ("%.8f" % (0.005/(float(bit_ask))+0.0001))
min_amount_2 = ("%.8f" % (0.005/(float(bit_ask))+0.0001))
buy_price = (float(bit_ask)-0.0001)
sell_price = (float(bit_bid)+0.0001)

def bit_sell_order():
	bit_trading_client.sell_limit_order(min_amount_2, sell_price)
	
def bit_buy_order():
	bit_trading_client.buy_limit_order(min_amount_1, buy_price)	

# Main Function ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def main():	
	while True:
		if R1>0.001:
			bit_sell_order()
			gem_buy_order()
			print ("TRADE MADE! R1:", arrow.now())	
			
		elif R2>0.001:
			bit_sell_order()
			gdax_buy_order()
			print ("TRADE MADE! R2:", arrow.now())
			
		elif R3>0.001:
			gem_sell_order()
			bit_buy_order()
			print ("TRADE MADE! R3:", arrow.now())
			
		elif R5>0.001:
			gdax_sell_order()
			bit_buy_order()
			print ("TRADE MADE! R5:", arrow.now())		
			
		elif R6>0.001:
			gdax_sell_order()
			gem_buy_order()
			print ("TRADE MADE! R6:", arrow.now())
		
		elif R4>0.001:
			gdax_buy_order()
			gem_sell_order()
			print ("TRADE MADE! R4:", arrow.now())
	
		else:
			print "...scanning trade conditions..."
		
		time.sleep(0.2)

main()
