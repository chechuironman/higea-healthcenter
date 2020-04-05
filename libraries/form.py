import json
import sys
from pymongo import MongoClient
import os
sys.path.append ("/project/userapp/libraries")

def form(form):

    try:
        connection = MongoClient(os.environ['MONGODB_HOST'],
                    username=os.environ['MONGODB_USER'],
                    password=os.environ['MONGODB_PASSWORD'],
                    authSource=os.environ['MONGODB_DATABASE'])
        # evaluation = evaluation(form)
        form["severity"] = evaluation(form)
        print(form)
        db = connection["higea"]
        collection = db["forms"]
        x = collection.insert_one(form)

        return True
    except:
        e = sys.exc_info()[0]
        print( "<p>Errorpid: %s</p>" % e )
        return str(0) 
def evaluation(form):
    try:
        if form['option3'] == 'yes' and form['option4'] == 'yes' and form['option1'] == 'yes':
            result = 'high'
        elif form['option3'] == 'yes' and form['option4'] == 'yes':
            result = "medium"
        else:
            result = "low" 
        return result
    except:
        e = sys.exc_info()[0]
        print( "<p>Errorpid: %s</p>" % e )
        return str(0) 