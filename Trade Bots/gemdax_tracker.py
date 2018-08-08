import gdax
import time, json, requests
import arrow
from geminipy import Geminipy

print "GDAX & Gemini Arbitrage Trading Bot v1.0"
print "created 8/31/2017 == xxx"
start_time = arrow.now()
print "Start Time:", start_time


"""
GET bid & asking prices
"""

con = Geminipy(api_key='xxx', secret_key='xxx', live=True)
gem_ticker_url = 'https://api.gemini.com/v1/pubticker/ethbtc'

public_client = gdax.PublicClient()
gdax_ticker_url = 'https://api.gdax.com/products/ETH-BTC/ticker'

while True:

	def gem_bid():
		ticker = requests.get(gem_ticker_url)
		return ticker.json() ['bid']

	def gem_ask():
		ticker = requests.get(gem_ticker_url)
		return ticker.json() ['ask']

	def gdax_bid():
		ticker = public_client.get_product_ticker('ETH-BTC')
		return ticker ['bid']

	def gdax_ask():
		ticker = public_client.get_product_ticker('ETH-BTC')
		return ticker ['ask']

	"""
	define ratios & order parameters
	"""

	gem_buy_price = (float(gem_bid())+0.00001) # exchange rate in BTC/ETH at which trade is opened
	gem_sell_price = (float(gem_ask())-0.00001)		# price offset shown in +/- BTC/ETH
	gdax_buy_price = (float(gdax_bid())+0.00001)
	gdax_sell_price = (float(gdax_ask())-0.00001)

	R1 = float((gdax_sell_price/gem_buy_price)*100-100.5)
	R2 = float((gem_sell_price/gdax_buy_price)*100-100.5)


	loop_time = arrow.now()

	if R1>0:
		print "Loop Time,", (loop_time - start_time), ",    R1,", ("%.4f" % R1)
	if R2>0:
		print "Loop Time,", (loop_time - start_time), ",    R2,", ("%.4f" % R2)


	time.sleep(0.2)
