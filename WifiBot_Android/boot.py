
# This file is executed on every boot (including wake-boot from deepsleep)

#Turn off debugging
import esp
esp.osdebug(None)

#Garbage collector
import gc
gc.collect()

#Setting Access Point
import uWifi_AP as Wifi_AP
Wifi_AP.ap_start()


