#!/usr/bin/env python
import time
import random
import RPi.GPIO as GPIO

# led-intensity.py
# Changes the intensity of a LED light. the intended goal is to create
# a "dimmer" effect on a led. for this program, the led will just
# change the intensity to a random value between 0 and 100 (or anything
# in between), and it will wait two seconds, and then perform the same
# change endlessly, until break is encountered.

GPIO.setmode(GPIO.BOARD)
# Change your PIN to the one you set in in your RPi.
PIN = 40
GPIO.setup(PIN, GPIO.OUT)
led = GPIO.PWM(PIN, 100)
# Start with Max Lighting (100% (see below))
led.start(100)
# Then wait two seconds..
time.sleep(2)
print('Changing the intensity to a random intensity value every ' +
      '2 seconds')
# This endless loop below is so the program continues to run
# indefinitely until you break it (usually ctrl-c)
run = True
try:
    while run:
        new_intensity = random.randint(10, 80)
        led.ChangeDutyCycle(new_intensity)
        time.sleep(2)
except KeyboardInterrupt:
    print('Exit Requested..')
    run = False
finally:
    # These are suggested to be used by the GPIO documentation.
    led.stop()
    GPIO.cleanup()
