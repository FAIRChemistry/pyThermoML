from flask_restful import Resource
from flask import request, send_file
from pythermo.thermoml.tools.writeTools import writeThermo
import json

class PostThermoML(Resource):

    def post(self): 
        jsonData = request.get_json()
        writeThermo(jsonData, 'newThermoFile')

        return send_file('newThermoFile.xml')