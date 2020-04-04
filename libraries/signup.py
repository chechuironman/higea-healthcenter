import json
import sys
from pymongo import MongoClient
import os
sys.path.append ("/project/userapp/libraries")

def signup(user,password):

    try:
        connection = MongoClient(os.environ['MONGODB_HOST'],
                    username=os.environ['MONGODB_USER'],
                    password=os.environ['MONGODB_PASSWORD'],
                    authSource=os.environ['MONGODB_DATABASE'])
        db = connection["higea"]
        collection = db["users"]
        x = collection.insert_one({"phone":user,"password":password})
        return True
    except:
        e = sys.exc_info()[0]
        print( "<p>Errorpid: %s</p>" % e )
        return str(0) 