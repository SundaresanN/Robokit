import dht
import machine
d = dht.DHT11(machine.Pin(4))
import dht
import machine
d = dht.DHT22(machine.Pin(4))
d.measure()
print('Temperature')
print(d.temperature())
print('Humidity')
print(d.humidity())

