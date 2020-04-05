from flask import Flask, redirect, jsonify
from flasgger import Swagger
from flask import request
from server import app
from server.routes.prometheus import track_requests
import sys
sys.path.append ("/project/userapp/libraries")
import helpers
import json
from flask_cors import CORS, cross_origin
import os
from logging.config import dictConfig
# The python-flask stack includes the flask extension flasgger, which will build
# and publish your swagger ui and specification at the /apidocs url. Here we set up
# the basic swagger attributes, which you should modify to match you application.
# See: https://github.com/rochacbruno-archive/flasgger
swagger_template = {
  "swagger": "2.0",
  "info": {
    "title": "Example API for python-flask stack",
    "description": "API for helloworld, plus health/monitoring",
    "contact": {
      "responsibleOrganization": "IBM",
      "responsibleDeveloper": "Henry Nash",
      "email": "henry.nash@uk.ibm.com",
      "url": "https://appsody.dev",
    },
    "version": "0.2"
  },
  "schemes": [
    "http"
  ],
}
swagger = Swagger(app, template=swagger_template)
app = Flask(__name__)
CORS(app)
# The python-flask stack includes the prometheus metrics engine. You can ensure your endpoints
# are included in these metrics by enclosing them in the @track_requests wrapper.
@app.route('/api/v1/login', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@track_requests
def _login():
    data  = json.loads(request.data.decode("utf-8"))
    print(data)
    result = login.login(data["phone"],data["password"])
    if result != False:
      app.logger.info('login, id %s succesful', data['phone'])
      return jsonify({"status": True,"id": result}), 200
    else:
      app.logger.info('login, id %s FAILED', data['phone'])
      return jsonify({"status": False}), 200

@app.route('/api/v1/signup', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@track_requests
def _signup():
    data  = json.loads(request.data.decode("utf-8"))
    signup_status = signup.signup(data["phone"],data["password"], dat["hospital"])
    app.logger.info('new user, id %s', signup_status)
    return jsonify({"id": signup_status}), 200

@app.route('/api/v1/insert_result', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@track_requests
def insert_result():
    data  = json.loads(request.data.decode("utf-8"))
    insert_result = helpers.insert_result(data["id"],data["result"])
    app.logger.info('new result, id %s', data["id"])
    return jsonify({"status": insert_result}), 200

@app.route('/api/v1/get_result', methods = ['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@track_requests
def get_result():
    data  = json.loads(request.data.decode("utf-8"))
    result = helpers.get_result(data["id"])
    app.logger.info('new result, id %s', data["id"])
    return jsonify({"id": result['id'], "status": result['result']}), 200

@app.route('/api/v1/healtcenters', methods = ['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@track_requests
def _healtcenters():
    healthcenters_list = helpers.healthcenter_list()
    app.logger.info('Healthcenters request')
    print(healthcenters_list)
    return healthcenters_list, 200

# It is considered bad form to return an error for '/', so let's redirect to the apidocs
@app.route('/')
def index():
    return redirect('/apidocs')

# If you have additional modules that contain your API endpoints, for instance
# using Blueprints, then ensure that you use relative imports, e.g.:
# from .mymodule import myblueprint
