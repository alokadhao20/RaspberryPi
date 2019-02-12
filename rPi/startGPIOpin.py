"""
20150214 - Created by stillborn86 (c)

This simple sketch is designed to blink an LED on and off using the GPIO of an
rPi system.  The GPIO pin can be changed to any general purpose pin the user
desires.  The same can be said about the delay between blinks.

"""

import time
import RPi.GPIO as GPIO

pin = 29  # This is the board number for which GPIO pin will be used
delay = 0.5  # This is the amount of delay (in seconds) between blinks

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

try:
    # while True:
    GPIO.output(pin, GPIO.HIGH)
    # time.sleep(delay)
    # GPIO.output(pin, GPIO.LOW)
    # time.sleep(delay)

except KeyboardInterrupt:
    print("\nA keyboard interrupt has been noticed")

except:
    print("\nAn error or exception has occurred!")

finally:
    GPIO.cleanup()
