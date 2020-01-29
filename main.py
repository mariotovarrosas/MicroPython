from wifi import do_connect
from machine import Pin
import time
import utime
import network
from funcion import *
import sys
T=0
contador = 0
tot=0
t = 0
def my_callback(l):
    global contador,tot
    contador = contador +1
    tot = contador


inpt = Pin(4, Pin.IN)
inpt.irq(trigger=Pin.IRQ_RISING, handler=my_callback)



sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

label  = 'Voltaje'
label1 = 'flujo'
data  = {label: 227}
data1 = {label1:227}
red = 'IER'
clave = 'acadier2014'

unique_id = '0e217ef0-3d47-11ea-9ffe-35550336f914'
token = 'zdOPgRd9KqHCcgKYRexa'

ap_if = network.WLAN(network.AP_IF)
sta_if.connect(red,clave)
cnt_boot = 0
cont = 0
print ("antes")

while True:
  T = ((contador*1.0)/320)
  t = ((tot* 60 )/ 6.6166666667)
  try:
    data[label] = T
    data1[label1] = t
    print("Publishing data")
    publish_thingsboard(token, unique_id,data)
#    publish_thingsboard(token, unique_id,data1)
    cnt_boot = 0
    contador = 0
    cont = 1
  except Exception as inst:
    print(inst)
    do_connect(red,clave);
    cnt_boot += 1
    cont += 1
    print("Fail {}".format(cnt_boot))
    if cont >1:
        contador = contador
    if cnt_boot > 10:
      machine.reset()
    time.sleep(1)
  time.sleep(30)
