import machine
led = machine.Pin(2, machine.Pin.OUT)
led.on()
led.off()
import time
while True:
  led.on()
  time.sleep(0.5)
  led.off()
  time.sleep(0.5)
