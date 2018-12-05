

import network
import sys
import time

def Wifi_Connect():
  WIFI_SSID = "<SSID>"
  WIFI_PASSWORD = "<Password>"
  
  # turn off the WiFi Access Point
  ap_if = network.WLAN(network.AP_IF)
  ap_if.active(False)
  
  # connect the device to the WiFi network
  wifi = network.WLAN(network.STA_IF)
  wifi.active(True)
  if(not wifi.isconnected()):
    wifi.connect(WIFI_SSID, WIFI_PASSWORD)
  
  # wait until the device is connected to the WiFi network
  while not wifi.isconnected():
    print('.')
    time.sleep(1)
 
  print('Wifi Connected')
  print('Network config: ',wifi.ifconfig())






