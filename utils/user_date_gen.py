import json
from faker import Faker
import os.path

current_dir = os.path.dirname(__file__)
date_file = os.path.join(current_dir, "user_data.json")


def generate_user_data(num_users):
    fake = Faker()
    user_data = []

    # Читаем существующие данные, если файл существует
    existing_data = []
    if os.path.exists(date_file):
        with open(date_file, 'r') as file:
            existing_data = json.load(file)

    # Генерируем новые данные
    for _ in range(num_users):
        user = {
            "First Name": fake.first_name(),
            "Last Name": fake.last_name(),
            "Email": fake.email(),
            "Password": fake.password(length=12)
        }
        user_data.append(user)

    # Объединяем старые и новые данные
    all_data = existing_data + user_data

    # Записываем обратно в файл
    with open(date_file, 'w') as file:
        json.dump(all_data, file, indent=4)