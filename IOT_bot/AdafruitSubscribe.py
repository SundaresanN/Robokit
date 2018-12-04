

import network
import time
from robust import MQTTClient
import os
import sys


Command1 = '$'
# the following function is the callback which is 
# called when subscribed data is received
def cb(topic, msg):
    print('Received Data:  Topic = {}, Msg = {}'.format(topic, msg))
    Command = str(msg,'utf-8')
    print('Command = {}'.format(Command))

# create a random MQTT clientID 
random_num = int.from_bytes(os.urandom(3), 'little')
mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')

def getCommand():
  #ADAFRUIT_IO_DETAILS
  ADAFRUIT_IO_URL = b'io.adafruit.com' 
  ADAFRUIT_USERNAME = b'ADAFRUIT USERNAME' #Enter your ADAFRUIT USERNAME
  ADAFRUIT_IO_KEY = b'ADAFRUIT AIO KEY' #Enter your ADAFRUIT AIO-KEY
  ADAFRUIT_IO_FEEDNAME = b'IO FEEDNAME'#Enter the FEEDNAME to be Monitored
  
  #CREATING OBJECT FOR MQTTClient Module
  client = MQTTClient(client_id=mqtt_client_id, 
                      server=ADAFRUIT_IO_URL, 
                      user=ADAFRUIT_USERNAME, 
                      password=ADAFRUIT_IO_KEY,
                      ssl=False)
  
  #Connecting to ADAFRUIT
  try:      
    client.connect()
  except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()
  print('Connected to adafruit')
  
  #Setting feedname
  mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME), 'utf-8')
  #setting a callback function for client object  
  client.set_callback(cb)
  print('callback set')
  
  #Subscribing For the Latest updated feed data
  client.subscribe(mqtt_feedname)
  print('Subscribed for data')
  mqtt_feedname_get = bytes('{:s}/get'.format(mqtt_feedname), 'utf-8')    
  client.publish(mqtt_feedname_get, '\0')  

  # wait until data has been Published to the Adafruit IO feed
  msg = client.wait_msg()
  Command1 = str(msg,'utf-8')
  client.disconnect()
  #returning the command to the My_BOT Module
  return Command1
