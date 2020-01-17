# Getting the libraries we need
from __future__ import print_function
import time
from gpiozero import DistanceSensor
from time import sleep
from grove.gpio import GPIO
from mraa import getGpioLookup
from grove.grove_led import GroveLed
from upm import pyupm_buzzer as upmBuzzer
from twython import Twython
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

# Initialize ultrasonic sensor
sensor = DistanceSensor(trigger=18, echo=24)
led = GPIO(16, GPIO.OUT)
pin = 12
mraa_pin = getGpioLookup("GPIO%02d" % pin)
buzzer = upmBuzzer.Buzzer(mraa_pin)
chords = [upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_DO];


while True:
	# Wait 2 seconds
    sleep(2)
	# Get the distance in metres
    distance = sensor.distance
	# But we want it in centimetres
    distance = sensor.distance * 100
	# We would get a large decimal number so we will round it to 2 places
    distance = round(sensor.distance, 2)

    print("Distance: {} cm".format(sensor.distance))
    
    if distance < 0.06:
        led.write(1)
        message = "La basura esta llena 2"
        twitter.update_status(status=message)
        print("Tweeted: {}".format(message))
        for chord_ind in range (0,3):
        # play each note for a half second
             print(buzzer.playSound(chords[chord_ind], 500000))
             time.sleep(0.1)
   
    else:
        led.write(0)



