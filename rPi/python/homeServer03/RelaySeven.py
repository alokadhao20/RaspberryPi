#!/usr/bin/env python
from flask_restful import Resource, Api
from flask import Flask, request, jsonify
import time
# import RPi.GPIO as GPIO
pin = 15
delay = 3

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(pin, GPIO.OUT)

class RelaySeven(Resource):
    def get(self, timeinhrs):
        try:
           print("RelaySeven" ,timeinhrs)
           if timeinhrs == 'off':
                print("RelaySeven timeinhrs")
                GPIO.output(pin, GPIO.LOW)
                GPIO.cleanup()
           else:
                print("Else")
                delay = int(timeinhrs) * 60
                print("delay - " ,delay)
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(delay)
                GPIO.output(pin, GPIO.LOW)
        except KeyboardInterrupt:
            print("\nA keyboard interrupt has been noticed")
        except:
            print("\nAn error or exception has occurred!")
        finally:
            print("finally")
            result = {'success':'true'}
            #GPIO.cleanup()
            return jsonify(result)
