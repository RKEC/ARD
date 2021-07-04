import socket
import os
import time
import psutil

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.2", 3132)) 

def destroy():
        print("goodbye :)")
        exit()

while True: 
    
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False


        full_msg += msg.decode("utf-8")
    
        if len(full_msg) - HEADERSIZE == msglen:
            print(full_msg[HEADERSIZE:])

            if "active" in full_msg:
                for process in psutil.process_iter():
                     if process.name() == "javaw.exe":
                        os.system("TASKKILL /im " + str(process.pid))
                        print("Task successfully stopped")
                        destroy()

            new_msg = True
            full_msg = ''

    print(full_msg)

    