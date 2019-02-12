#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET
import time
import RPi.GPIO as GPIO

pin = 29  # This is the board number for which GPIO pin will be used
delay = 0.5  # This is the amount of delay (in seconds) between blinks

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

urls = (
    '/light/start', 'light_start',
    '/light/stop', 'light_stop'
)

app = web.application(urls, globals())

class light_start:        
    def GET(self):
        try:
            # while True:
            print("light start")
            GPIO.output(pin, GPIO.HIGH)
            # time.sleep(delay)
            # GPIO.output(pin, GPIO.LOW)
            # time.sleep(delay)

        except KeyboardInterrupt:
            print("\nA keyboard interrupt has been noticed")

        except:
            print("\nAn error or exception has occurred!")

        finally:
            #GPIO.cleanup()
            return True;
	
class light_stop:        
    def GET(self):
        try:
            # while True:
            # GPIO.output(pin, GPIO.HIGH)
            # time.sleep(delay)
            GPIO.output(pin, GPIO.LOW)
            # time.sleep(delay)

        except KeyboardInterrupt:
            print("\nA keyboard interrupt has been noticed")

        except:
            print("\nAn error or exception has occurred!")

        finally:
            #GPIO.cleanup()
            return True;
# class get_user:
#     def GET(self, user):
# 	for child in root:
# 		if child.attrib['id'] == user:
# 		    return str(child.attrib)

if __name__ == "__main__":
    app.run()