"""
20150214 - Created by stillborn86 (c)

This simple sketch is designed, much like the blink sketch, to fade an LED on
and off at a pre-determined rate.  This rate, as well as which GPIO pin, can be
determined by the end-user.

"""

import time
import RPi.GPIO as GPIO

pin = 7
# This is the GPIO attached to the LED

fade = 10
# This is the rate the LED will fade -- Larger numbers will fade faster, smaller
# numbers will fade slower

brightness = 0
# This is the initial brightness setting for the LED -- it is best to leave this
# at zero.

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        GPIO.output(pin, brightness)
        brightness = brightness + fade
        if (brightness <= fade-1 or brightness >= 254-fade):
            fade = -fade
    time.sleep(0.03)

except KeyboardInterrupt:
    print("\nA keyboard interrupt has been detected!")

except:
    print("\nAn error or exception has occurred!")

finally:
    GPIO.cleanup()
