import machine
import time
button = machine.Pin(12, machine.Pin.IN,machine.Pin.PULL_UP)
led = machine.Pin(14, machine.Pin.OUT)
button.value()
while True:
  val=button.value()
  if not val :
    led.value(1)
    print("rec")
  else:
    led.value(0)
    print("nrecv")
  
  
  time.sleep(0.5)
  
 
  

