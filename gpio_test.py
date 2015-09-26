# gpio_test.py
# by Jasper Meurs
# LED is on pin 17

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

state = True

# endless loop, on/off for 1 second
while True:
	GPIO.output(17, True)
	time.sleep(1)
	GPIO.output(17, False)
	time.sleep(1)