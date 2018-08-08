import bitstamp.client

trading_client = bitstamp.client.Trading(username='xxx', key='L8OLdTCVcVrafH2brfDtfibVtlbIW9w0', secret='xxx')
print (trading_client.ticker()['last'])
