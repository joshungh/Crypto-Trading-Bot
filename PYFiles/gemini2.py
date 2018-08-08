from geminipy import Geminipy

con = Geminipy(api_key='xxx', secret_key='xxx', live=True)
symbols = con.symbols()
book = con.book()


x = 0.079
def gem_buy_order():
	order = con.new_order(amount=0.01, price=x, side='buy')

gem_buy_order()
