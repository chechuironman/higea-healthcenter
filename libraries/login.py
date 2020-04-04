import json
import sys
from pymongo import MongoClient
sys.path.append ("/project/userapp/libraries")

def login(user,password):

    try:
        connection = MongoClient(os.environ['MONGODB_HOST'],
                    username=os.environ['MONGODB_USER'],
                    password=os.environ['MONGODB_PASSWORD'],
                    authSource=os.environ['MONGODB_DATABASE'])
        collection = db["users"]
        x = collection.find_one({"user":user})
        print(x)
        # return(json.dumps(namespace_))
    except:
        e = sys.exc_info()[0]
        print( "<p>Errorpid: %s</p>" % e )
        return str(0) 