# 20141129 - Created by stillborn86 (c)

# This script sets up randomly "dancing" LED's on GPIO 11, 12, 13, and 15 by
# turning them on and off randomly.

import time
import random
import RPi.GPIO as GPIO

GPIO.setup(11,GPIO.OUT)  # Set up GPIO pins as outputs
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

try:
    while True:
        x = random.randint(11,15)  # Pick a random pin
        y = random.randint(11,15)
        if (x != y and x != 14 and y != 14): # Avoid pin 14 and similar LEDs
            GPIO.output(x, GPIO.HIGH)  # Turn random LED on
            GPIO.output(y, GPIO.HIGH)
            time.sleep(0.15)  # Pause
            GPIO.output(x, GPIO.LOW)  # Turn random LED off
            GPIO.output(y, GPIO.LOW)

except KeyboardInterrupt:
    print("\nA keyboard interrupt has been detected!")

except:
    print("\nAn error or exception has occurred!")

finally:
    GPIO.cleanup()
