import bitstamp.client
import time, json, requests
import arrow
from geminipy import Geminipy

print "Bitstamp & Gemini Arbitrage Trading Bot v1.0"
print "created 8/30/2017 == xxx"
start_time = arrow.now()
print "Start Time:", start_time

con = Geminipy(api_key='xxx', secret_key='xxx', live=True)
gem_ticker_url = 'https://api.gemini.com/v1/pubticker/ethbtc'

bit_public_client = bitstamp.client.Public()
bit_trading_client = bitstamp.client.Trading(
	username='xxx', key='xxx', secret='xxx')

# GET bid & asking prices
def gem_bid():
	ticker = requests.get(gem_ticker_url)
	return ticker.json() ['bid']

def gem_ask():
	ticker = requests.get(gem_ticker_url)
	return ticker.json() ['ask']

bit_bid = bit_public_client.ticker()['bid']

bit_ask = bit_public_client.ticker()['ask']

# define ratios & order parameters
bit_buy_price = (float(bit_bid)+0.000001) # in BTC/ETH, e.g. 0.08000 BTC/ETH.
bit_sell_price = float(bit_ask)
gem_buy_price = (float(gem_bid())+0.00001)
gem_sell_price = float(gem_ask())

R1 = float((bit_sell_price/gem_buy_price)*100-100.5)
R2 = float((gem_sell_price/bit_buy_price)*100-100.5)

min_amt_1 = ("%.6f" % (0.005/(float(gem_buy_price)))) #in ETH
min_amt_2 = ("%.6f" % (0.005/(float(bit_buy_price))))
btc_amt_1 = (float(min_amt_1)*float(gem_buy_price))
btc_amt_2 = (float(min_amt_2)*float(bit_buy_price))


# POST buy & sell orders
def gem_buy_order():
	order = con.new_order(amount=min_amt_1, price=gem_buy_price, side='buy')
	print "GEMINI: bought", min_amt_1, "ETH for", btc_amt_1, "BTC --- Rate, ETH/BTC =", gem_buy_price

def gem_sell_order():
	order = con.new_order(amount=min_amt_2, price=gem_sell_price, side='sell')
	print "GEMINI: sold", min_amt_2, "ETH for", btc_amt_2, "BTC --- Rate, ETH/BTC =", gem_buy_price

def bit_sell_order():
	bit_trading_client.sell_limit_order(min_amt_1, bit_sell_price)
	print "BITSTAMP: sold", min_amt_1, "ETH for", btc_amt_1, "BTC --- Rate, ETH/BTC =", gem_buy_price

def bit_buy_order():
	bit_trading_client.buy_limit_order(min_amt_2, bit_buy_price)
	print "BITSTAMP: bought", min_amt_1, "ETH for", btc_amt_2, "BTC --- Rate, ETH/BTC =", gem_buy_price

while True:
	if R1>0:
		print "R1:", "%.5f" % R1
	if R2>0:
		print "R2:", "%.5f" % R2

	time.sleep(0.3)

Main()
