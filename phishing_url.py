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
uri = "mongodb+srv://rha:Ash332577@phishingcluster.yow9qr6.mongodb.net/?retryWrites=true&w=majority&appName=PhishingCluster"
password = "Ash332577"
client = MongoClient(uri)

db = client["url_data"]


# add data to MongoDB route
@app.route('/add_url_data', methods = ['POST'])
def add_url_data():
    # get data from request

    # gets the 'email' from the url

    collection = db['url_data']

    email = request.args.get('email')
    survey_ID = request.args.get('survey_ID')
    source = request.args.get('source')

    print(email, survey_ID, source)

    sampleURL = URLdata(survey_ID,"www.gmail.com",1,source,[email])
    hashInput = survey_ID + source

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
