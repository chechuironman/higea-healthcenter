import json
import sys
import uuid 
from pymongo import MongoClient
import os
sys.path.append ("/project/userapp/libraries")

def signup(user,password):

    try:
        if validNumber(user):
            connection = MongoClient(os.environ['MONGODB_HOST'],
                        username=os.environ['MONGODB_USER'],
                        password=os.environ['MONGODB_PASSWORD'],
                        authSource=os.environ['MONGODB_DATABASE'])
            db = connection["higea"]
            collection = db["users"]
            id = uuid.uuid1() 
            x = collection.find_one({"phone":user})
            if x:
                return False
            else:
                x = collection.insert_one({"id":id,"phone":user,"password":password})
                return id
        else:
            return False
    except:
        e = sys.exc_info()[0]
        print( "<p>Errorpid: %s</p>" % e )
        return str(0) 

def validNumber(phone_number):
    if len(phone_number) != 9:
        return False
    if phone_number[0] != '6':
        return False
    if isinstance(phone_number, int):
        return False
    return True