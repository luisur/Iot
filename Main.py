#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import time
from grove.gpio import GPIO
from grove.grove_led import GroveLed
from gpiozero import DistanceSensor
import Adafruit_DHT
from twython import Twython
from mraa import getGpioLookup
from upm import pyupm_buzzer as upmBuzzer

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
#    sensor = sensor_args[sys.argv[1]]
#    pin = sys.argv[2]
#else:
#    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
#    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
 #   sys.exit(1)

sensor = 11
pin = 24
pinBuzzer = 12
sensorDistancia = DistanceSensor(trigger=18, echo=24)
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
led1 = GPIO(26, GPIO.OUT)
led2 = GPIO(16, GPIO.OUT)

mraa_pin = getGpioLookup("GPIO%02d" % pinBuzzer)
buzzer = upmBuzzer.Buzzer(mraa_pin)
chords = [upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_MI,
              upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_MI,
              upmBuzzer.BUZZER_DO];

#Humidity = AdafruitDHT.humidity
#Temperature = AdafruitDHT.temperature
cont = 0
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    distance = sensor.distance
    distance = sensor.distance * 100
    distance = round(sensor.distance, 2)
    if distance < 0.01:
         led2.write(1)
    else:
         led2.write(0)
    print("Distance: {} cm".format(sensor.distance))
    cont+=1
    print(cont)
    if cont < 2:
        message = ('La actual4343 temperatura es de {}º y la humedad es de {}%'.format(temperature, humidity))
        twitter.update_status(status=message)
        print("Tweeted: {}".format(message))
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    #print("La distancia es: {} cm".format(distanceSensor.distance))
    if temperature > 25:
        led1.write(1)
        for chord_ind in range (0,7):
            # play each note for a half second
            print(buzzer.playSound(chords[chord_ind], 500000))
            time.sleep(0.1)
        del buzzer
        #print ('LED ON...')
        time.sleep(1)
    else:
        led1.write(0)
        #print ('LED OFF...')
        time.sleep(1)

    

