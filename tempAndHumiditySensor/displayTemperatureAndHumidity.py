#!/usr/bin/python
import sys
import Adafruit_DHT
import time
import datetime
while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        if humidity is not None and temperature is not None:
                now = datetime.datetime.now()
                print now.strftime("%Y-%m-%d %H:%M")
                print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
                time.sleep(30)
                print 'after sleep'
        else:
                print 'Failed to get reading. Try again!'
