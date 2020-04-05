import json
import sys
from pymongo import MongoClient
import os
sys.path.append ("/project/userapp/libraries")

def login(user,password):

    try:
        connection = MongoClient(os.environ['MONGODB_HOST'],
                    username=os.environ['MONGODB_USER'],
                    password=os.environ['MONGODB_PASSWORD'],
                    authSource=os.environ['MONGODB_DATABASE'])
        db = connection["higea"]
        collection = db["users"]
        x = collection.find_one({"phone":user,"password":password})
        if x:
            logged = x['id']
        else:
            logged = False    
        return logged
    except:
        e = sys.exc_info()[0]
        print( "<p>Errorpid: %s</p>" % e )
        return str(0) 