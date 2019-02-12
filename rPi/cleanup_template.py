"""
2015XXxx - Created by stillborn86 (c)

This sketch is designed...

"""

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

try:
    while True:


except KeyboardInterrupt:
    print("\nA keyboard interrupt has been detected!")

except:
    print("\nAn error or exception has occurred!")

finally:
    GPIO.cleanup()
