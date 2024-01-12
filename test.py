from faker import Faker
from pymongo import MongoClient
from datetime import datetime
import creds
from datetime import datetime
import urllib
import random


fake = Faker()

mongo_uri = f"mongodb+srv://{urllib.parse.quote(creds.user)}:{urllib.parse.quote(creds.paasword)}@poccluster.sjsfbns.mongodb.net/?retryWrites=true&w=majority"
print(mongo_uri)