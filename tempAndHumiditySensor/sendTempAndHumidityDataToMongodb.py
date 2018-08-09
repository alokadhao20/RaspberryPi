#!/usr/bin/python

# install module 
# install pip 
# https://pip.pypa.io/en/stable/installing/
# install pymongo

import sys
import Adafruit_DHT
import time
import datetime

import pymongo
from pymongo import MongoClient
from datetime import datetime
client = MongoClient('mongodb://alok:noguess21@ds137019.mlab.com:37019/tempandhumidity')


# Get the sampleDB database
db = client.tempandhumidity

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

result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)