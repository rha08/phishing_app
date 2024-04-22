from flask import Flask, request
from pymongo import MongoClient
import hashlib

def hash(hashInput):
    primary_key = hashlib.sha256(hashInput.encode())
    return primary_key.hexdigest()

class URLdata():
    def __init__(self, survey_ID, url, count_of_users, source, users_info):
        self.survey_ID = survey_ID
        self.url = url
        self.count_of_users = count_of_users
        self.source = source
        self.users_info = users_info



# Flask app object
app = Flask(__name__)

# set up the MongoDB connection
client = MongoClient('mongodb://localhost:27017')

db = client["url_data"]


# add data to MongoDB route
@app.route('/add_url_data', methods = ['POST'])
def add_url_data():
    # get data from request

    collection = db['url_data']

    sampleURL = URLdata("survey003","www.yahoo.com",1,"Email",["Rhea"])
    hashInput = sampleURL.survey_ID + sampleURL.url + sampleURL.source

    data = {
        "_id": hash(hashInput),
        "survey_ID" : sampleURL.survey_ID,
        "url": sampleURL.url,
        "count_of_users": sampleURL.count_of_users,
        "source": sampleURL.source,
        "users_info": sampleURL.users_info
    }

    res = collection.find({"_id": hash(hashInput)})
    count = 0
    for key in res:
       count = count + 1

    if count == 0:
        collection.insert_one(data)
    else:
        cursor = collection.find_one({"_id":hash(hashInput)})
        users = cursor["users_info"]
        users.extend(sampleURL.users_info)
        collection.update_one({"_id": hash(hashInput)}, {"$set":{"count_of_users":cursor["count_of_users"]+1}})
        collection.update_one({"_id": hash(hashInput)}, {"$set":{"users_info":users}})

    return 'Data added to MongoDB'

if __name__ == "__main__":
    app.run()


"""
### primary key:
unique key: (URL + Source + Survey_ID)

Hash Function: used to convert URL + Source + Survey_ID to an encrypted string value (Ex. ufweifuhwfed)

"""

"""
TASK

current state: simple insert

TASK ONE:

While inserting, check if the primary key is present or not already in the database
If present:
    1. Increase count
    2. Add user

Otherwise:
    1. Do a fresh insert

https://towardsdatascience.com/using-mongo-databases-in-python-e93bc3b6ff5f


TASK TWO:

Host my project at github and send it to sir via mail.
pulkit.jetlearn@gmail.com
"""