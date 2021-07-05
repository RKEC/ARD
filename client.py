import socket
import os
import time
import psutil

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server's ip, port
#port can be changed if already used (has to be changed on both server and client)
s.connect(("server's ip", 1111)) 

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
                    for process in psutil.process_iter():
                        #looks for minecraft's process id
                        if process.name() == "javaw.exe":
                            os.system("TASKKILL /im " + str(process.pid))
                            print("Task successfully stopped")
                              

                new_msg = True
                full_msg = ''

        print(full_msg)

except KeyboardInterrupt:
        destroy()   
