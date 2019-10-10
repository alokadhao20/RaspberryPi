import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library

ESC=4  #Connect the ESC in this GPIO pin 

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0)

max_value = 2000 #change this if your ESC's max value is different or leave it be - PPM , Throttle
min_value = 1100  #change this if your ESC's min value is different or leave it be - PPM , Throttle

pi.set_servo_pulsewidth(ESC, 0)
pi.set_servo_pulsewidth(ESC, max_value)
pi.set_servo_pulsewidth(ESC, min_value)
print "Wierd eh! Special tone"
time.sleep(14)
print "See.... uhhhhh"
# print "Wait for it ...."
# time.sleep (5)
# print "Im working on it, DONT WORRY JUST WAIT....."
# pi.set_servo_pulsewidth(ESC, 0)
# pi.set_servo_pulsewidth(ESC, min_value)
# time.sleep(1)
# print "See.... uhhhhh"