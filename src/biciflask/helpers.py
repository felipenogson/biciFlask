from faker import Faker
import json

fake = Faker()

def rider_generator():
    rider = str.lower(f'{fake.first_name()}-{fake.word()}-{fake.last_name()}-{fake.email()}-{fake.ssn()}')
    rider = json.dumps({'rider':rider})
    return rider

if __name__ == "__main__":
    pass


