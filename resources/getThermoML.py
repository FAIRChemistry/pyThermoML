from flask_restful import Resource
from flask import request, send_file
from pythermo.thermoml.tools.readTools import readThermo
import json

class GetThermoML(Resource):

    def get(self):
        file = request.files()
        #print(file)
        dataReport = readThermo(file)
        print(dataReport)
        return "a"