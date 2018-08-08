import bitstamp.client
import time, json, requests
import arrow

bit_public_client = bitstamp.client.Public()

trading_client = bitstamp.client.Trading(
	username='xxx', key='L8OLdTCVcVrafH2brfDtfibVtlbIW9w0', secret='xxx')

bit_bid = bit_public_client.ticker()['bid']
bit_ask = bit_public_client.ticker()['ask']
min_amount_1 = ("%.8f" % (0.005/(float(bit_ask))+0.0001))
min_amount_2 = (0.005/float(bit_ask))
buy_price = (float(bit_ask)-0.00001)
sell_price = (float(bit_ask)-0.000001)

print bit_bid
print bit_ask

def bit_sell_order():
	trading_client.sell_limit_order(min_amount_2, sell_price)

def bit_buy_order():
	trading_client.buy_limit_order(min_amount_1, buy_price)

bit_buy_order()
