#!/usr/bin/env python
from flask_restful import Resource, Api
from flask import Flask, request, jsonify
# import RPi.GPIO as GPIO
pin = 29
delay = 3

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(pin, GPIO.OUT)

class RelayEight(Resource):
    def get(self, state):
        try:
            print("RelayEight state - ", state)
            if state == 'on':
                print("on")
                # GPIO.output(pin, GPIO.HIGH)
            elif state == 'off':
                print("off")
                # GPIO.output(pin, GPIO.LOW)
            else:
                print("We can't decide.")
        except KeyboardInterrupt:
            print("\nA keyboard interrupt has been noticed")
        except:
            print("\nAn error or exception has occurred!")
        finally:
            print("finally")
            result = {'success':'true'}
            #GPIO.cleanup()
            return jsonify(result)
            
