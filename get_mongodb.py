from pymongo import MongoClient


user ='admin'
password = 'admin'

mongo_uri = f"mongodb+srv://{(user)}:{(password)}@poccluster.sjsfbns.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri)
db = client["centric_poc_0"]
collection = db["dummy_orders"]

print(collection)

# db.collection.find

# print(dummy_orders)
collection.insert_many(dummy_orders)
client.close()
