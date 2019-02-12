#!/usr/bin/env python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import atexit
# from sqlalchemy import create_engine
from json import dumps
# from Employees_Name import Employees_Name
from RelayEight import RelayEight
from RelaySeven import RelaySeven


# db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__, static_url_path='')
api = Api(app)
api.add_resource(RelayEight, '/light/<state>')
api.add_resource(RelaySeven, '/charger/<timeinhrs>')


def close_running_threads():
    print "Threads complete, ready to finish"
#Register the function to be called on exit
atexit.register(close_running_threads)




if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5002, threaded=True)
