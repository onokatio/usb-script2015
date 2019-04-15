#! /usr/bin/env /usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(20, GPIO.OUT)

while True:

    GPIO.output(20, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(20, GPIO.LOW)
    time.sleep(1)

#except KeyboardInterrupt:
#  GPIO.cleanup()
