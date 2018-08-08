import time
import sys, getopt
import datetime

def main(argv):
	period = 10
	
	try:
		opts, args = getopt.getopt(argv,"hp:",["period=",])
	except getopt.GetoptError:
		print ('bot1.py -p <period>')
		sys.exit(2)
		
	for opt, arg in opts:
		if opt == '-h':
			print ('bot1.py -p <period>')
			sys.exit()
		elif opt in ("-p", "--period"):
			if (int(arg) in [300,900,1800,7200,14400,86400]):
				period = arg
			else:
				print ('Poloniex requires 300, 900, 1800, 7200, 14400, or 86400 seconds')
				sys.exit(2)
	
	while True:
		print ("{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " Period: %ss")
		time.sleep(int(period))


if __name__ == "__main__":
	main(sys.argv[1:])
	
	