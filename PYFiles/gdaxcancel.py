#GDAX Trading Bot 1.0
#last updated 8/20/2017

import gdax

public_client = gdax.PublicClient()

#public API requests

currenttime = public_client.get_time()
btcTicker = public_client.get_product_ticker('BTC-USD')

#private API requests == need to consult JU & KS regarding privacy & proper encryption

auth_client = gdax.AuthenticatedClient('xxx', 'xxx', 'xxx')


auth_client.cancel_order("#enter transaction id")
