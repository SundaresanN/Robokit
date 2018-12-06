#hardware platform: FireBeetle-ESP8266

import machine 
import time

IR=machine.Signal(15,machine.Signal.IN)           #create Button object from pin15,Set Pin15 to input (D4)
led=machine.Signal(13,machine.Signal.OUT)             #create LED object from pin13,Set Pin13 to output (D2)

while True:
  a=led.value(IR.value())     #Gets the state of the Button and passes the state to the LED
  if a==1:
    print("Obstacle")
  else:
    print("Nothing")
  time.sleep(0.1)
