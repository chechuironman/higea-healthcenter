import json
import sys
from pymongo import MongoClient
import os
from bson.json_util import dumps
from bson.json_util import loads
from bson import json_util
sys.path.append ("/project/userapp/libraries")

def healthcenter_list():

    try:
        connection = MongoClient(os.environ['MONGODB_HOST'],
                    username=os.environ['MONGODB_USER'],
                    password=os.environ['MONGODB_PASSWORD'],
                    authSource=os.environ['MONGODB_DATABASE'])
        db = connection["healthcenters"]
        collection = db["healthcenters"]
        document = collection.find()
        return dumps(document)
    except:
        e = sys.exc_info()[0]
        print( "<p>Errorpid: %s</p>" % e )
        return str(0) 
def insert_result(id,result):
    try:
        connection = MongoClient(os.environ['MONGODB_HOST'],
                    username=os.environ['MONGODB_USER'],
                    password=os.environ['MONGODB_PASSWORD'],
                    authSource=os.environ['MONGODB_DATABASE'])
        db = connection["healthcenters"]
        collection = db["results"]
        document = collection.insert_one({"id":id,"result":result})
        return True
    except:
        e = sys.exc_info()[0]
        print( "<p>Errorpid: %s</p>" % e )
        return str(0) 

def get_result(id):
    try:
        connection = MongoClient(os.environ['MONGODB_HOST'],
                    username=os.environ['MONGODB_USER'],
                    password=os.environ['MONGODB_PASSWORD'],
                    authSource=os.environ['MONGODB_DATABASE'])
        db = connection["healthcenters"]
        collection = db["results"]
        document = collection.find_one({"id":id})
        return {"id":document['id'],"result":document['result']}
    except:
        e = sys.exc_info()[0]
        print( "<p>Errorpid: %s</p>" % e )
        return str(0) 