"""
20150127 - Created by RaspberryPiIVBeginners
https://www.youtube.com/watch?v=S2v1VNgHnvI

Modified by stillborn86 (c)

This sketch is designed to read a Ds18b20 18b20 Thermometer Temperature Sensor
(http://www.amazon.com/gp/product/B00OZGWWQA?psc=1) connected to Pin7, and
report back a current temperature in both celsius as well as fahrenheit.

"""

# Importing libraries necessary for functionality
import os
import glob
import time

# Initialize the device
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# This section looks for the physical device within your Linux system
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# Defined function to retrieve temperature sensor data
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines  # Return the value to the calling function

# Defined function to take data from read_temp_raw() and convert it into
# human-readable data
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0  # Convert data to celsius
        temp_f = temp_c * 9.0 / 5.0 + 32.0  # Convert celsius to fahrenheit
        return temp_c, temp_f  # Return both temps to the calling function

try:
    # Defined function to continuounly fetch temperature data from reat_temp()
    # every second
    while True:
        print(read_temp())
        time.sleep(1)

except KeyboardInterrupt:
    print("\nA keyboard interrupt has been detected!")

except:
    print("\nAn error or exception has occurred!")

finally:
    GPIO.cleanup()
