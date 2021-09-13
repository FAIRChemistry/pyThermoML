from flask import Flask
from flask_restful import Api

from resources import GetThermoML, PostThermoML

app = Flask(__name__)
api = Api(app=app)

api.add_resource(PostThermoML, "/files")
api.add_resource(GetThermoML, "/files")

if __name__ == "__main__":
    app.run(
        debug=True
    )
