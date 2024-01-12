from faker import Faker
from datetime import datetime
import random

fake = Faker()

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
        "coordinates": {
            "latitude": fake.latitude(),
            "longitude": fake.longitude(),
        },
    },
    "inserted_at": datetime.utcnow(),  # Timestamp for insertion
    "phone_numbers": [
        fake.phone_number(),
        fake.phone_number(),
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

print(employee_data)
