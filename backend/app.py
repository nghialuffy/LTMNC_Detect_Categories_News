#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from datetime import datetime
from Controller.homepage import HomePage
from Controller.detect_category import DetectCategory

app = Flask(__name__)
api = Api(app)


api.add_resource(HomePage, '/') # Home page 
api.add_resource(DetectCategory, '/api/v1.0/detect_category')

if __name__ == '__main__':
    try:
        app.debug = True
        app.run(host='0.0.0.0', port=8001) # api Dev
    except Exception as e:
        print('Error: ', e)
        

