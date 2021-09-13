from flask_restful import Resource
from flask import request, send_file
from pythermo.thermoml.tools.writeTools import writeThermoFromJSON
import json

class PostThermoML(Resource):

    def post(self): 
        jsonData = request.get_json()
        writeThermoFromJSON(jsonData, 'newThermoFile')

        return send_file('newThermoFile.xml')
    

