import bitstamp.client
import time, json, requests
import arrow
from geminipy import Geminipy

print "Bitstamp & Gemini Arbitrage Trading Bot v1.0"
print "created 8/30/2017 == xxx"
start_time = arrow.now()
print "Start Time:", start_time

con = Geminipy(api_key='ivrwpKOnNKTNCcLNvvwV', secret_key='xxx', live=True)
gem_ticker_url = 'https://api.gemini.com/v1/pubticker/ethbtc'

bit_public_client = bitstamp.client.Public()
bit_trading_client = bitstamp.client.Trading(
	username='xxx', key='xxx', secret='xxx')

while True:

	def gem_bid():
		ticker = requests.get(gem_ticker_url)
		return ticker.json() ['bid']

	def gem_ask():
		ticker = requests.get(gem_ticker_url)
		return ticker.json() ['ask']

	bit_bid = bit_public_client.ticker()['bid']

	bit_ask = bit_public_client.ticker()['ask']

	bit_buy_price = (float(bit_bid)+0.000001)
	bit_sell_price = float(bit_ask)
	gem_buy_price = (float(gem_bid())+0.00001)
	gem_sell_price = float(gem_ask())

	R1 = float((bit_sell_price/gem_buy_price)*100-100.5)
	R2 = float((gem_sell_price/bit_buy_price)*100-100.5)

	if R1>0:
		print "R1:", "%.5f" % R1, "TIME:", arrow.now()
	if R2>0:
		print "R2:", "%.5f" % R2, "TIME:", arrow.now()

	time.sleep(0.2)
