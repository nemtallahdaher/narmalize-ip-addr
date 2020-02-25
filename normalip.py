#!/usr/bin/python
import sys
import socket
import struct


try:

	def ip2long(ip):
		"""
		Convert an IP string to long
		"""
		packedIP = socket.inet_aton(ip)
		return struct.unpack("!L", packedIP)[0]
		
	def long2ip(ipdec):
		"""
		Convert an IP long to string
		"""
		return socket.inet_ntoa(struct.pack('!L', ipdec))

		
	def normalip(iplistdec):
		normalizedip = []
		iplistdec.sort()
		startingip = 0
		j = 0
		for i in iplistdec:
			j += 1
			if startingip == 0:
				startingip = i
				lastip = i
			else:
				if lastip + 1 == i:
					lastip = i
				else:
					if startingip != lastip:
						normalizedip.append(long2ip(startingip)+'-'+long2ip(lastip))
					else:
						normalizedip.append(long2ip(lastip))
					startingip = i
					lastip = i
		if j == len(iplistdec):
			if startingip != lastip:
				normalizedip.append(long2ip(startingip)+'-'+long2ip(lastip))
			else:
				normalizedip.append(long2ip(lastip))
		return normalizedip

		
	# Produce Normal IP
	ip = input("Enter IP List: ")
	ip = ip.replace(" ","")
	iplist = ip.split(",")
	iplistdec = []
	for ipaddr in iplist:
		iplistdec.append(ip2long(ipaddr))
	ipliststr = ','.join(normalip(iplistdec))
	print ("Results: ", ipliststr)


except Exception as e:
  sys.stderr.write('---Error: '+str(e)+'\n')


