## NOTE: run as sudo, otherwise you might not see all the networks

from wifi import Cell, Scheme
import sys, socket
from time import sleep
from urllib2 import urlopen, URLError, HTTPError

done = False
halfPage = "\n\n\n\n\n\n\n\n\n\n"

def is_connected():
		url = 'http://google.com'
		try:
				response = urlopen( url )
		except HTTPError:
				print '1 Internet Down. Setup starting...\n'
			return False
	except URLError:
				print '2 Internet Down. Setup starting... \n'
			return False
	else:
				html = response.read()
				responseurl = response.url
				if response.url.startswith('http://www.google'):
						print "Internet connected"
						return True
				else:
						print "3 Internet down. Setup starting... \n"
			return False

done = is_connected()

while (done != True):
		try:
				getOut = 0
				allCells = Cell.all('wlan0')
				print halfPage
				print "Choose a network by number:\n\n"
				for i in range(len(allCells)):
						print i, allCells[i].ssid
				networkNumber = input(halfPage)
				cell = allCells[networkNumber]
				if cell.encrypted:
						passkey = raw_input('Enter Password:\n')
				else:
						passkey = ''
				scheme = Scheme.for_cell('wlan0', 'home', cell, passkey)
				try:
						scheme.save()
				except Exception as e:
						pass

				while (getOut < 2):
						try:
								scheme.activate()
								getOut = 2
						except Exception as ex:
								getOut += 1
								print 'Error:', ex
								print getOut
								pass
				print 'Done with connection loop.'
		done = is_connected()
		except:
				print 'Unkown Error...  :('
				done = True