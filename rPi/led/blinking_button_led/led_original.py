# I uploaded the code only because I don't have the board to simulate the led 
# controlling behaviour 
# Hardware : 
# - connect a button to pin 12 of raspberry and other button terminal to ground   
#    through 1kohm resistor
# - connect the led cathode to pin 13 while the anode pin connected to 3.3V 
#   through 10KOhm resistor 
 
#To access the GPIO from python
import RPi.GPIO as GPIO
#to enable to use delays
import time  
 
ReadValue = 1;
 
#use the bin numbering as counted on board  
GPIO.setmode(GPIO.BOARD)
 
#to set pin directions to be input/output 
GPIO.setup (12, GPIO.IN)
GPIO.setup (13, GPIO.OUT)
     
 
#to out low on pin 13 (to turn led on)  
GPIO.output(13,False)
 
while (1):
    #to check the state of button 
    ReadValue = GPIO.input(12)
    # if no button pressed,then blinking
    while ReadValue != 0:
        #to out high on pin 13 which should turn off the led 
        GPIO.output(13,True) 
        #wait one second
        time.sleep(1)
        #to out low on pin 13 (to turn led on)  
        GPIO.output(13,False)
        #wait one second
        time.sleep(1)
        #read the input (button state) again
        ReadValue = GPIO.input(12)
     
    ##the following lines will be executed iff a button is pressed 
    #to out low on pin 13 (to turn led on)  
    GPIO.output(13,False)
