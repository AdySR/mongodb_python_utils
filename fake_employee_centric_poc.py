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
collection = db["dummy_employees"]


employee_documents=[]
for _ in range(3):
    employee_data = {
    "name": fake.name(),
    "email": fake.email(),
    "position": fake.job(),
    "salary": fake.random_int(min=30000, max=100000),
    "address": {
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "zipcode": fake.zipcode(),
    },
    "inserted_at": datetime.utcnow().isoformat(),
    "phone_numbers": [
        fake.phone_number(),
    ],
    "skills": [
        {"name": fake.job(), "level": random.choice(["Beginner", "Intermediate", "Advanced"])},
        {"name": fake.job(), "level": random.choice(["Beginner", "Intermediate", "Advanced"])},
        {"name": fake.job(), "level": random.choice(["Beginner", "Intermediate", "Advanced"])},
    ],
    "education": {
        "degree": fake.random_element(["Bachelor's", "Master's", "Ph.D."]),
        "major": fake.job(),
        "university": fake.company(),
        "graduation_year": fake.random_int(min=2000, max=2023),
        "additional_info": {
            "thesis_topic": fake.sentence(),
            "advisor": fake.name(),
        },
    },
}


    employee_documents.append(employee_data)


# print(employee_documents)
collection.insert_many(employee_documents)
client.close()