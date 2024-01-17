from faker import Faker
import time
import json

fake = Faker()

def rider_generator():
    rider = str.lower(f'{fake.first_name()}-{fake.word()}-{fake.last_name()}-{fake.email()}-{time.time_ns()}')
    rider = json.dumps({'rider':rider})
    return rider

if __name__ == "__main__":
    pass


