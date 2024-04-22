# Data Modelling

"""
To define the parameters/attributes that needs to be persisted for an application

Attributes:

Survey_ID
Attached_Link (Malicious Link/Test Link)
Count_Of_Users_Clicked
Source (Email, Message, Etc.)
Users_Info (List)

Data Storages:

Where do we store data?
Storage Accessible via Internet -> Cloud Databases

1. SQL (Structured Query Language) [used for data defined in multiple tables and is interconnected]

Usecases: Banking, Ticket Booking, Transactional Usecase

2. NoSQL [used for cases where there are no transactions needed and no interconnection between the data]

For our case: NoSQL
1. Easy and faster delivery
2. We don't have transactional data


# API: Application Programming Interface (The way with which we interact with some defined request or addresses that are exposd to the world to
access applications' functions)

Software:

- MongoDB - NoSQL Storage
- TinyUrl: To shorten URL links
- Postman: API Testing Framework (Click APIs )

"""


"""
TASK:

1. Research Flask
2. Practice making APIs
3. Make a connection to Mongo DB

LINKS:

https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/
https://www.w3schools.com/python/python_mongodb_getstarted.asp
https://www.geeksforgeeks.org/sending-data-from-a-flask-app-to-mongodb-database/


4. Create a Post API -> to insert the above data model model to Mongo DB
(the list of attributes above )

    - if the server and link are already there, then increase the count and add the additional user.
    (if the link has alr been clicked before)
    - If the server and link are not there, then make an entry with all info

5. Download Postman

"""


