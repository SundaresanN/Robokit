

import network

def ap_start():
  #configuring access point
  ap = network.WLAN(network.AP_IF)
  #Resetting AP
  ap.active(False)
  ap.active(True)
  #configuring ssid and password
  ap.config(essid = 'RC-CAR')
  ap.config(authmode =3 ,password = '123456789')
  #printing ip address
  print('network config:',ap.ifconfig())




