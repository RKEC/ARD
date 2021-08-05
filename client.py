import socket
import os
import time
import psutil

HEADERSIZE = 10
games = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 1110)) 

def destroy():
        print("goodbye :)")
        exit()
try:
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
                    with open('gamesPiD.txt', 'r') as f:
                        games = f.readlines()
                    
                
                for process in psutil.process_iter():
                     for game in games:
                        print(process.name() + " " + game)
                        if process.name().__eq__(game):
                                os.system("TASKKILL /im " + str(process.pid) + "/T /F")
                                process.kill()
                                print("Task successfully stopped")

                new_msg = True
                full_msg = ''

        print(full_msg)

except KeyboardInterrupt:
        destroy()
    
