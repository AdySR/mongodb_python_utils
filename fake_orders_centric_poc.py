from faker import Faker
from pymongo import MongoClient
from datetime import datetime
import creds
from datetime import datetime
import urllib
import random


fake = Faker()

mongo_uri = f"mongodb+srv://{urllib.parse.quote(creds.user)}:{urllib.parse.quote(creds.paasword)}@poccluster.sjsfbns.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri)
db = client["centric_poc_0"]
collection = db["dummy_orders"]


dummy_orders=[]
for _ in range(300000):
    order_document = {
        'order_number': fake.random_int(min=1000, max=9999),
        'customer_name': fake.name(),
        'product': fake.word(),
        'quantity': fake.random_int(min=1, max=10),
        "inserted_at": datetime.utcnow().isoformat()
    }


    dummy_orders.append(order_document)


# print(dummy_orders)
collection.insert_many(dummy_orders)
client.close()

