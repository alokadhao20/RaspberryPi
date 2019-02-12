# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BOARD)
from urlparse import urlparse, parse_qs
pin = 29

class light_start:        
    def GET(self, employee_id):
        try:
            # Or use the parse_qs method
            # query_components = parse_qs(urlparse(self.path).query)
            # imsi = query_components["imsi"]
            # imsi = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('imsi', None)
            # query_components = { "imsi" : ["Hello"] }
            # while True:
            # GPIO.output(pin, GPIO.HIGH)
            print("light_start",employee_id)
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