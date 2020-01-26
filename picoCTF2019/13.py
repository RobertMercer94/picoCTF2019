from pwn import *

s= remote('chall.pwnable.tw', 10000)

print(s.recv())

s.sendline('yo')

print(s.recv())
print(s.recv())
print(s.recv())


s.close