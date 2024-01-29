from faker import Faker
from pymongo import MongoClient
from random import randint, choice
from datetime import datetime, timedelta
import json

client = MongoClient("mongodb+srv://admin:admin@poccluster.sjsfbns.mongodb.net/?retryWrites=true&w=majority", 27017)
db = client['centric_poc_0']
collection = db['dummy_employees']
fake =Faker()

employees=[]
def generate_fake_employee():
    for _ in range(10):
        employee = {
            "name": fake.name(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "address": {
                "street": fake.street_address(),
                "city": fake.city(),
                "state": fake.state(),
                "zipcode": fake.zipcode(),
            },
            "job_title": fake.job(),
            "salary": fake.random_int(min=30000, max=100000),
            "inserted_at": datetime.utcnow().isoformat(),
        }
        employees.append(employee)
    
    return employees



collection.insert_many(generate_fake_employee())
client.close()
