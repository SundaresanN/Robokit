from machine import Pin,I2C
import RGB1602
import time
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

print("========IOT BASIC KIT ESP8266 I2C LCD1602 TEST===========")
lcd=RGB1602.RGB1602(16,2,i2c)
lcd.setRGB(0,50,0);
lcd.setCursor(0,0)
lcd.print("IOT Basic Kit")

lcd.setCursor(5,1)
lcd.print("SASTRA")
while True:
    time.sleep(1)
    lcd.scrollDisplayLeft()
    
