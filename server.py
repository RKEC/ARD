import socket
import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

blue = 22
green = 27
red = 17
HEADERSIZE = 10

GPIO.setup(4, GPIO.IN)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 1122))
s.listen(5)
def destroy():
        GPIO.output(red, 0)
        GPIO.output(green, 0)
        GPIO.output(blue, 0)
        print("goodbye :)")
        GPIO.cleanup()
        socket.close()

try:
        while True:
                clientsocket, address = s.accept()
                print(f"Connection from {address} established")
                message = ''
                while True:
                        if GPIO.input(4) == GPIO.HIGH:
                                message = "active"
                                print("active")
                                GPIO.output(red, 255)
                                GPIO.output(green, 0)
                                GPIO.output(blue, 0)
                                time.sleep(1.5)
                                message = f'{len(message):<{HEADERSIZE}}' + message    
                                clientsocket.send(bytes(message, "utf-8"))
            
                        else:
                                message = "idle"
                                GPIO.output(red, 0)
                                GPIO.output(green, 0)
                                GPIO.output(blue, 255)
                                time.sleep(1.25)
                                GPIO.output(red, 0)
                                GPIO.output(green, 0)
                                GPIO.output(blue, 0)
                                time.sleep(1)
                
                
except KeyboardInterrupt:
        destroy()   
