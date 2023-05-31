import json
from faker import Faker

fake = Faker()

names = []
for i in range(500):
    name = fake.name()
    names.append({'name': name, 'value': None})

with open('names.json', 'w') as f:
    for name in names:
        f.write(json.dumps(name) + '\n')