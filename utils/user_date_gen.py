import json
from faker import Faker
import os.path

current_dir = os.path.dirname(__file__)
date_file = os.path.join(current_dir, "user_data.json")


def generate_user_data(num_users):
    fake = Faker()
    user_data = []

    for _ in range(num_users):
        user = {
            "First Name": fake.first_name(),
            "Last Name": fake.last_name(),
            "Email": fake.email(),
            "Password": fake.password(length=12)
        }
        user_data.append(user)

    with open(date_file, 'w') as file:
        json.dump(user_data, file, indent=4)
