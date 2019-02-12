from flask_restful import Resource, Api
from flask import Flask, request, jsonify
class Employees_Name(Resource):
    def get(self, employee_id):
        # conn = db_connect.connect()
        # query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        # result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        result = {'data':employee_id}
        return jsonify(result)