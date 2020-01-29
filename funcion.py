def settimeout(duration):
  pass
def t3_publication(topic, msg):
  print (topic, ';', msg)
  pycom.rgbled(0xff00)


def publish_thingsboard(token,UNIQUE_ID,data, password=''):
  from umqtt.simple import MQTTClient
  import gc
  import json
  import machine
  import utime
  client = MQTTClient(UNIQUE_ID, "iot.ier.unam.mx", port = 1883, user=token, password=password)
  client.settimeout = settimeout
  client.connect()
  print(json.dumps(data))
  client.publish('v1/devices/me/telemetry', json.dumps(data) )
  client.disconnect()
