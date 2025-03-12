from faker import Faker
import random

fake = Faker()

def generate_sample_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "name": fake.name(),
            "email": fake.email(),
            "age": random.randint(18, 35),
        }
        data.append(record)

if __name__ == "__main__":
    sample_data = generate_sample_data(100)
    for record in sample_data:
        print(record)
    