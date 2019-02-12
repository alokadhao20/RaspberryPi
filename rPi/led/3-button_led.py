"""
20160518 - Created by stillborn86 (c)

This sketch is designed to control three independent LEDs using three
different pushbuttons.  Each button press will turn an assigned LED on, and a
subsequent button press will then turn that assigned LED off.

LEDs will be connected to pins 11, 13, and 15
Buttons will be connected to 29, 31, and 33
"""

#import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

# Set each GPIO color to a pin number
RedL = 11
YellowL = 13
GreenL = 15

# Assign each pushbutton GPIO as a color
RedB = 29
YellowB = 31
GreenB = 33

# Assign initial LED states
RedLED = False
YellowLED = False
GreenLED = False

# Set each GPIO pin as an appropriate input/output
GPIO.setup(RedL, GPIO.OUT)
GPIO.setup(YellowL, GPIO.OUT)
GPIO.setup(GreenL, GPIO.OUT)
GPIO.setup(RedB, GPIO.IN)
GPIO.setup(YellowB, GPIO.IN)
GPIO.setup(GreenB, GPIO.IN)

try:
    while True:
        # Set all LEDs to their assigned states
        GPIO.output(RedL, RedLED)
        GPIO.output(YellowL, YellowLED)
        GPIO.output(GreenL, GreenLED)

        # Read each button for a button press event
        ReadValueR = GPIO.input(RedB)
        ReadValueY = GPIO.input(YellowB)
        ReadValueG = GPIO.input(GreenB)

        # If a button is pressed, reverse the state of the LED variable
        if (ReadValueR == 0):
            RedLED ^= 1
        elif (ReadValueY == 0):
            YellowLED ^= 1
        elif (ReadValueG == 0):
            GreenLED ^= 1

# Stop the sketch if a keyboard interrupt (^C) is entered
except KeyboardInterrupt:
    print("\nA keyboard interrupt has been detected!")

# Stop the sketch if a problem/error occurs
except:
    print("\nAn error or exception has occurred!")

# Clean up GPIO for future use
finally:
    GPIO.cleanup()
