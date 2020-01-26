from pwn import *
import os

#l=listen()

#s = remote('2019shell1.picoctf.com', 49816)
#s = ssh(host= '2019shell1.picoctf.com', user = 'nitro8', password = 'superstar1')

os.system('cd BinaryExploitation; ls')
os.system('file vuln6')
#s('ls')

#print(s.recv())



#s.close()
