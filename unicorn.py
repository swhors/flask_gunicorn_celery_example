from flask import Flask, Blueprint
import flask_restful
import flask_cors
from flask_restful import Resource, request
import os,sys
import logging

errors = {
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400,
    },
    "InvalidDateTimeFormatError": {
        "message": "Invalid input syntax for type timestamp with time zone",
        "status": 400,
    },
    "InvalidIntegerFormatError": {
        "message": "Invalid input syntax for type integer",
        "status": 400,
    },
    "DuplicateIdError": {
        "message": "Request Parameter(user_id) is duplicated",
        "status": 400,
    },
}


def create_flask():
    app = Flask(__name__)
    app.logger.setLevel(logging.DEBUG)
    from testapi1 import TestApi_New, TestApi_Old, Api_StudentAdd
    flask_cors.CORS(app, resources={r"/*": {"origins": "*"}})
    device_api_blueprint = Blueprint( "device_api", __name__, url_prefix="/api")
    device_api = flask_restful.Api(device_api_blueprint, errors=errors)

    device_api.add_resource(TestApi_Old, "/test/old")
    device_api.add_resource(TestApi_New, "/test/new")
    device_api.add_resource(Api_StudentAdd, "/student/insert/<name>/<grade>")
    app.register_blueprint(device_api_blueprint)
    return app


app = create_flask()


if __name__=="__main__":
    #app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=True, threaded=True)
    app.run(host="0.0.0.0")
