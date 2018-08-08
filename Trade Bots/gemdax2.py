import gdax
import time, json, requests
import arrow
from geminipy import Geminipy

print "GDAX & Gemini Arbitrage Trading Bot v1.2"
print "created 9/1/2017 == xxx"
start_time = arrow.now()
print "Start Time:", start_time


"""
GET bid & asking prices
"""

con = Geminipy(api_key='xxx', secret_key='xxx', live=True)
gem_ticker_url = 'https://api.gemini.com/v1/pubticker/ethbtc'

auth_client = gdax.AuthenticatedClient('xxx', 'xxx', 'xxx')
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

	gem_buy_price = (float(gem_bid())) # exchange rate in BTC/ETH at which trade is opened
	gem_buy_price2 = (float(gem_bid())+0.00002)
	gem_sell_price = (float(gem_ask()))		# price offset shown in +/- BTC/ETH
	gdax_buy_price = (float(gdax_bid())+0.00001)
	gdax_sell_price = (float(gdax_ask()))

	R1 = float((gdax_sell_price/gem_buy_price)*100-100.5)
	R2 = float((gem_sell_price/gdax_buy_price)*100-100.5)

	min_amt = 0.01 #size of trade in ETH to be bought and sold for BTC; Gemini: >=0.001 ETH, GDAX: >=0.01 ETH

	btc_amt_1 = (min_amt*float(gem_buy_price)) #amount of BTC bought/sold for "min_amt"
	btc_amt_2 = (min_amt*float(gem_sell_price))
	btc_amt_3 = (min_amt*float(gdax_sell_price))
	btc_amt_4 = (min_amt*float(gdax_buy_price))

	if R1>0:

		def gdax_sell_order():
			auth_client.sell(price=gdax_sell_price,
							 size=min_amt,
							 product_id='ETH-BTC')
		def gem_buy_order():
			order = con.new_order(amount=min_amt, price=gem_buy_price, side='buy')
			print "GEMINI, buy,", min_amt, ", ETH,", btc_amt_1, "BTC --- Rate, ETH/BTC =", gem_buy_price

		def gem_buy_order2():
			order = con.new_order(amount=min_amt, price=gem_buy_price2, side='buy')
			print "GEMINI, buy,", min_amt, ", ETH,", btc_amt_1, "BTC --- Rate, ETH/BTC =", gem_buy_price

		gdax_sell_order()
		gdax_sell_order()
		gdax_sell_order()
		gem_buy_order()
		gem_buy_order()
		gem_buy_order2()

		print "GDAX: sold", min_amt, "ETH for", btc_amt_3, "BTC --- Rate, ETH/BTC =", gdax_sell_price

	elif R2>0:

		def gem_sell_order():
			order = con.new_order(amount=min_amt, price=gem_sell_price, side='sell')
			print "GEMINI: sold", min_amt, "ETH for", btc_amt_2, "BTC --- Rate, ETH/BTC =", gem_sell_price

		def gdax_buy_order():
			auth_client.buy(price=gdax_buy_price,
							size=min_amt,
							product_id='ETH-BTC')

		gem_sell_order()
		gem_sell_order()
		gem_sell_order()
		gdax_buy_order()
		gdax_buy_order()
		gdax_buy_order()

		print "GDAX: bought", min_amt, "ETH for", btc_amt_4, "BTC --- Rate, ETH/BTC =", gdax_buy_price

	time.sleep(0.2)
