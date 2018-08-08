import bitstamp.client
import time, json, requests
import arrow
import gdax

#BITSTAMP

bit_public_client = bitstamp.client.Public()


bit_bid = bit_public_client.ticker()['bid']
bit_ask = bit_public_client.ticker()['ask']


bit_trading_client = bitstamp.client.Trading(
	username='xxx', key='xxx', secret='xxx')


def bit_buy():
	price = float(bit_bid)*1.0001
	x = round(price, 6)
	min_amount = 0.005/float(bit_bid)
	bit_trading_client.buy_limit_order("%.8f" % min_amount, x)
	print price
	print min_amount


bit_buy()







#GDAX gdax_public_client = gdax.PublicClient()
