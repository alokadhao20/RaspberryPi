from flask_restful import Resource, Api
from flask import Flask, request, jsonify
class RelayEight(Resource):
    def get(self):
        # conn = db_connect.connect()
        # query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        # result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        try:
            # while True:
            GPIO.output(pin, GPIO.HIGH)
            # time.sleep(delay)
            # GPIO.output(pin, GPIO.LOW)
            # time.sleep(delay)

        except KeyboardInterrupt:
            print("\nA keyboard interrupt has been noticed")
            

        except:
            print("\nAn error or exception has occurred!")

        finally:
            print("finally")
            result = {'success':'true'}
            return jsonify(result)
            #GPIO.cleanup()
            # return True;
            # result = {'success':'true'}
            # return jsonify(result)