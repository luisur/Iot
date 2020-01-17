#!/usr/bin/python

import sys
import time
import Adafruit_DHT
from grove.grove_led import GroveLed


# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
sensor = 11
pin = 24
led1 = GPIO(26, GPIO.OUT)
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

     if temperature > 29:
         led1.write(1)
     else:
         led1.write(0)
         

     if humidity is not None and temperature is not None:
         print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
         print('Funciona')
         time.sleep()
     else:
         print('Failed to get reading. Try again!')
         sys.exit(1)
