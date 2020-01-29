# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import os
import time
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("WIFI-CIE-UNAM-101", "")
wlan.isconnected()
wlan.ifconfig()
