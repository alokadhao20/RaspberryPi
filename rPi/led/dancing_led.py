# 20141129 - Created by stillborn86 (c)

# This script sets up randomly "dancing" LED's on GPIO 11, 12, 13, and 15 by
# turning them on and off randomly.

import time
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)  # Set up GPIO pins as outputs
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

try:
    while True:
        x = random.randint(11,15)  # Pick a random pin
        if x != 14:  # Avoid pin 14
            GPIO.output(x, GPIO.HIGH)  # Turn random LED on
            time.sleep(0.09)  # Pause
            GPIO.output(x, GPIO.LOW)  # Turn random LED off

except KeyboardInterrupt:
    print("\nA keyboard interrupt has been detected!")

except:
    print("\nAn error or exception has occurred!")

finally:
    GPIO.cleanup()
