#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Adafruit_DHT
import time

# temp-humidity.py
# This script uses the Adafruit DHT library to read the values
# of temperature and humidity of the DHT11 or DHT22 sensor.

SENSOR = Adafruit_DHT.DHT22
# Even though the API mentions the PIN here, it is actually the GPIO# e.g.
# GPIO22 for the Raspberry Pi, Remember that GPIO "numbers" don't correspond
# to the physical PIN numbers on the GIPO board on the RPi.
PIN = 22
DEG_SYMBOL = u'\u00b0'

while True:
    # read_retry(sensor, pin)
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    if humidity is not None and temperature is not None:
        # Temp, is given in Celsius, give the information in Fahrenheit as well
        f_deg = (temperature * 1.8) + 32
        print(u'Temperature: {0:0.1f}{1}C / {2:0.1f}{1}F - '
              'Humidity={3:0.1f}%'.format(
                temperature, DEG_SYMBOL, f_deg, humidity))
        time.sleep(3)
    else:
        print('Failed to get reading. Try again!')
