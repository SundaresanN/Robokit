import machine
led = machine.Signal(14, machine.Pin.OUT, invert = True)
led.on()
led.off()
import time
while True:
  led.on()
  time.sleep(0.5)
  led.off()
  time.sleep(0.5)

