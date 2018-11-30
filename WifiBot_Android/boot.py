









# This file is executed on every boot (including wake-boot from deepsleep)

import esp

esp.osdebug(None)

import gc

gc.collect()


import uWifi_AP as Wifi_AP

Wifi_AP.ap_start()


