# I uploaded the code only because I don't have the board to simulate the led 
# controlling behaviour 
# Hardware : 
# - connect a button to pin 12 of raspberry and other button terminal to ground 
#    through 1kohm resistor
# - connect the led cathode to pin 13 while the anode pin connected to 3.3V 
#   through 10KOhm resistor 

"""
20160124
All code scanned and modified by stillborn86 (c)

This sketch is designed to blink an LED until a pushbutton is pressed.  At that
time, the blinking will stop until the pushbutton is pressed again.  A secondary
press will initiate the blinking once again.

"""

# To access the GPIO from python
import RPi.GPIO as GPIO
# To enable to use delays
import time

# Set initial value for pushbutton and run variables
ReadValue = 0
run = 1

# Use the bin numbering as counted on board
GPIO.setmode(GPIO.BOARD)

# To set pin directions to be input/output
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.OUT)

def blink():
    while (run == 1):
        # Set LED to on and wait one second
        GPIO.output(13,1)
        time.sleep(1)
        # Set LED to off and wait one second
        GPIO.output(13,0)
        time.sleep(1)

# Create multithreading for simultaneous processes
from threading import Thread
t1 = blink()
#t2 = Thread(target=read)

# Start blinking threaded processes
t1.start()

try:
    while True:
        ReadValue = GPIO.input(12)

        if(ReadValue == 1):
            if(run == 0):
                run = 1
                t1.start()
            elif(run == 1):
                run = 0
                t1._stop()
                GPIO.output(13,0)
            ReadValue = 0

except KeyboardInterrupt:
    print("\nA keyboard interrupt has been detected!")

except:
    print("\nAn error or exception has occurred!")
    
finally:
    GPIO.cleanup()

