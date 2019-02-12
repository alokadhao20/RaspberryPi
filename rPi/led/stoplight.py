# 20141129

# This program simulates the red, yellow, green cycle of a traffic light.

import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

red = 11  # Set GPIO pin numbers as colors
yellow = 13
green = 15

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

try:
    while True:
        GPIO.output(red, HIGH)
        time.sleep(2)
        GPIO.output(red, LOW)
        GPIO.output(green, HIGH)
        time.sleep(2)
        GPIO.output(green, LOW)
        GPIO.output(yellow, HIGH)
        time.sleep(.5)
        GPIO.output(yellow, LOW)

except KeyboardInterrupt:
    print("\nA keyboard interrupt has been detected!")

except:
    print("\nAn error or exception has occurred!")

finally:
    GPIO.cleanup()
