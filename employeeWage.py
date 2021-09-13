'''
@Author: Javeed
@Date: 2021-09-11 
@Last Modified by: Javeed
@Last Modified time: 2021-09-12 14:54:00
@Title : EmployeeWage
'''
import random
from flask_restful import Resource, Api
from flask import Flask,jsonify,request

app = Flask(__name__)
api = Api(app)
emp_data = []

@app.route('/')
def welcome():
    '''
            Description:
                get function to welcome 
            Parameter:
                None
            Return:
                Note
    '''
    return "Welcome to the Employee Wage"

@app.get("/data")
def get_data():
    '''
            Description:
                get function is use to only read the data 
            Parameter:
                None
            Return:
                data
    '''
    return jsonify(emp_data)

class employee(Resource):
    
    def get(self,name):
        '''
            Description:
                get function is use to only read the data 
            Parameter:
               name as input
            Return:
                data
        '''
        for i in emp_data:
            if i['Data'] == name:
                return i
        return {'Data': None}

    def post(self,name):
        '''
            Description:
                post function is use to add the data  
            Parameter:
               name as input
            Return:
                data
        '''
        full_time = 0
        part_time = 1
        check = random.randint(0,2)
        if ( full_time == check ) :
            status= "present" 
            Tem_emp_data = {'Data':name,'Wage' : 20*8,'Status' : status,'Employee_Work':'Full-Time'}
        elif(part_time == check):
            status= "present" 
            Tem_emp_data = {'Data':name,'Wage' : 20*4,'Status' : status,'Employee_Work':'Part_time'}
        else:
            status = "Absent"
            Tem_emp_data = {'Data':name,'Wage' : 20*0,'Status' : status,'Employee_Work':status}

        emp_data.append(Tem_emp_data)
        return Tem_emp_data
    
    def delete(self,name):
        '''
            Description:
                function to delete the value 
            Parameter:
               name as input
            Return:
                data
        '''
        for index,i in enumerate(emp_data):
            if i['Data'] == name:
                emp_data.pop(index)
                return {'Note':"Deleted"}
 
api.add_resource(employee,'/Name/<string:name>')

if __name__ == '__main__':
    app.run(debug = True)