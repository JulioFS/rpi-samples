#!/usr/bin/env python
import RPi.GPIO as GPIO

# led-on-off.py
# This is a very basic, interactive script that turns a led on, or off
# Note that it uses Python 2.7+ raw_input() method, accomodate for this
# if using this script under python 3+

# Tell the GPIO to use the PIN numbering schema for the RPi
GPIO.setmode(GPIO.BOARD)

# GPIO21, respectively below:
PIN = 40

# Setup the pin to use as output (lights)
GPIO.setup(PIN, GPIO.OUT)

run = True
try:
    while run:
        command = raw_input('Select \'on\', or \'off\', \'q\' to quit: ')
        if command.lower() == 'on':
            # Turn the pin/led "on"
            GPIO.output(PIN, GPIO.HIGH)
        elif command.lower() == 'off':
            # Turn the pin/led off
            GPIO.output(PIN, GPIO.LOW)
        elif command.lower() == 'q':
            run = False
except KeyboardInterrupt:
    print('Exit Requested..')
    run = False
finally:
    GPIO.cleanup()
