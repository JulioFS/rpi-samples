import time
import RPi.GPIO as GPIO

# servo.py
# Still under construction, operating of a servo motor using the RPi 3

GPIO.setmode(GPIO.BOARD)
pin = 32
GPIO.setup(pin, GPIO.OUT)
servo = GPIO.PWM(pin, 100)
servo.start(7.5)
run = True
try:
    while run:
        servo.ChangeDutyCycle(7.5) # Neutral
        time.sleep(1)
        servo.ChangeDutyCycle(12.5) # 180 deg
        time.sleep(1)
        servo.ChangeDutyCycle(2.5) # 0 deg
        time.sleep(1)
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
    print('Exiting..')
