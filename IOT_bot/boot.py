



# This file is executed on every boot (including wake-boot from deepsleep)

import esp

esp.osdebug(None)

import gc
#initiating GARBAGE COLLECTION
gc.collect()


#Connecting to WIFI
import Wifi_Station as Wifi

Wifi.Wifi_Connect()









