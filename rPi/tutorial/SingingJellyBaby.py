# First we need to import the libraries that
# we need

# Import the time library so that we can make
# the program pause for a fixed amount of time
import time

# Import the Raspberry Pi GPIO libraries that
# allow us to connect the Raspberry Pi to
# other physical devices via the General
# Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO

# Import the os library so that we can make
# our program call other programs that run on
# the Raspberry Pi
import os

# Now we need to set-up the General Purpose
# Input-Output (GPIO) pins

# Clear the current set-up so that we can
# start from scratch
GPIO.cleanup()

# Set up the GPIO library to
# use Raspberry Pi board pin
# numbers
GPIO.setmode(GPIO.BOARD)

# Set pin 3 on the GPIO header to be an input
GPIO.setup(3,GPIO.IN)

# This loop runs forever and plays the mp3
# file when the two wires are touching
while True:

    # Check to see if pin 3 on the GPIO
    # header is connected to the ground pin
    if GPIO.input(3) == False:

        # If it's connected to ground
        # then play the mp3 file
        os.system('mpg321 la.mp3 &')

    # Wait for a second before repeating
    # the loop
    time.sleep(1)
