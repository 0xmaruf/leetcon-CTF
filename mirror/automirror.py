from pwn import *

p = remote("103.191.240.170",9999)

print(p.recvline())
while(1):
	s = p.recvline()
	print(s)
	s = str(s.decode()).replace("\n","",)
	print(s[::-1])
	p.sendline(s[::-1].encode())

