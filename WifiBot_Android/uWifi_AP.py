

import network
def ap_start():
  ap = network.WLAN(network.AP_IF)
  ap.active(False)
  ap.active(True)
  ap.config(essid = 'RC-CAR')
  ap.config(authmode =3 ,password = '123456789')
  print('network config:',ap.ifconfig())




