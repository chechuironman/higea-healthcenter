from flask import Flask, redirect, jsonify
from flasgger import Swagger
from flask import request
from server import app
from server.routes.prometheus import track_requests
import sys
# import kubernetes
sys.path.append ("/project/userapp/libraries")
import login,signup
import json
from flask_cors import CORS, cross_origin
import os
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
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


# cors = CORS(app, resources={r"/": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'
app = Flask(__name__)
CORS(app)

# The python-flask stack includes the prometheus metrics engine. You can ensure your endpoints
# are included in these metrics by enclosing them in the @track_requests wrapper.
@app.route('/hello')
@track_requests
def HelloWorld():
    # To include an endpoint in the swagger ui and specification, we include a docstring that
    # defines the attributes of this endpoint.
    """A hello message
    Example endpoint returning a hello message
    ---
    responses:
      200:
        description: A successful reply
        examples:
          text/plain: Hello from Appsody!
    """
    return 'Hello from Appsody!'


@app.route('/api/v1/form', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@track_requests
def _form():
    data  = json.loads(request.data.decode("utf-8"))
    print(data)
    app.logger.info('new form, id %i', 1)
    return jsonify({"id":1,"result": data['data']}), 200


@app.route('/api/v1/signup', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@track_requests
def _signup():
    data  = json.loads(request.data.decode("utf-8"))
    signup_status = signup.signup(data["phone"],data["password"])
    app.logger.info('new user, id %i', data['phone'])
    return jsonify({"result": signup_status}), 200

@app.route('/api/v1/login', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@track_requests
def _login():
    data  = json.loads(request.data.decode("utf-8"))
    print(data)
    result = login.login(data["phone"],data["password"])
    app.logger.info('login, id %i', data['phone'])
    return jsonify({"status": result}), 200

@app.route('/')
def index():
    return redirect('/apidocs')

# If you have additional modules that contain your API endpoints, for instance
# using Blueprints, then ensure that you use relative imports, e.g.:
# from .mymodule import myblueprint
