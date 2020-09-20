import pymongo
import os

if os.path.exists("env.py"):
    import env


MONGODB_URI = os.environ.get("MONGO_URI")
DBS_NAME = "myFirstDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# INSERT ONE DOCUMENT
# # insert is depreciated use insert_one or insert_many

# new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952',
#            'hair_colour': 'grey', 'occupation': 'writer',
#            'nationality': 'english'}
# coll.insert_one(new_doc)

# INSERT MANY DOCUMENT
# new_docs = [
#             {'first': 'terry', 'last': 'pratchett',
#              'dob': '28/04/1948', 'gender': 'm',
#              'hair_colour': 'not much', 'occupation': 'writer',
#              'nationality': 'english'},
#             {'first': 'george', 'last': 'rr martin',
#              'dob': '20/09/1948', 'gender': 'm', 'hair_colour': 'white',
#              'occupation': 'writer', 'nationality': 'american'}
#            ]
# coll.insert_many(new_docs)

# REMOVE SPECIFIC DOCUMENTS
# # remove  deprecated use delete_one or delete_many
# coll.delete_one({'first': 'douglas'})

# UPDATE ONE DOCUMENT
# coll.update_one({'nationality': 'american'},
#                 {'$set': {'hair_colour': 'maroon'}})

# UPDATE MANY DOCUMENTS
coll.update_many({'nationality': 'american'},
                 {'$set': {'hair_colour': 'blue'}})


# FIND SPECIFIC DOCUMENTS
documents = coll.find({'nationality': 'american'})

# FIND ALL DOCUMENTS
# documents = coll.find()

for doc in documents:
    print(doc)
