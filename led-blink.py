#!/usr/bin/env python
import time
import random
import RPi.GPIO as GPIO

# led-blink.py
# From a selection of 5 LEDs, blink them alternatively by randomly
# turning each one on and off, while pausing on every loop. The
# intention of this script is to create an "alarm" system for a model
# house which will make all lights blink in rapide succession.

# Tell the GPIO to use the PIN numbering schema for the Rpi
GPIO.setmode(GPIO.BOARD)

# GPIO17, GPIO18, GPIO27, GPIO23, and GPIO21, respectively below:
PINS = [11, 12, 13, 16, 40]

# Setup the pins to use as output (lights)
# setup() takes a single value or a list
GPIO.setup(PINS, GPIO.OUT)

# This endless loop below is so the program continues to run
# indefinitely until you break out of it..
run = True
try:
    while run:
        # Get a random pin
        led = random.choice(PINS)
        # Turn the pin/led "on"
        GPIO.output(led, GPIO.HIGH)
        # Wait a bit..
        time.sleep(0.15)
        # Then tun the pin/led off, then loop back to get another
        # random pin, note that the random function can return the same
        # pin again, but it should be enough to give the blinking illusion.
        GPIO.output(led, GPIO.LOW)
except KeyboardInterrupt:
    print('Exit Requested..')
    run = False
finally:
    GPIO.cleanup()
