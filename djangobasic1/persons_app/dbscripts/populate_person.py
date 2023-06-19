'''
    Python manage.py shell
    execute the below command inside the shell
    exec(open('./persons_app/dbscripts/populate_person.py').read())
'''

from faker import Faker
from persons_app.models import Person

MAX_LIMIT = 1000
AGES = [i for i in range(1,99)]

fake = Faker()

class PopulatePerson:
    def __init__(self):
        pass

    def fetch_random_age(self):
        return fake.random_choices(elements=AGES, length=1)
    
    def run(self):
        Faker.seed(0)
        for i in range(1, MAX_LIMIT):            
            age = self.fetch_random_age()[0]
            profile = fake.simple_profile()
            print(f"Name: {profile['name']} and age {profile['birthdate']}")
            Person.objects.create(
                name = profile['name'],
                age = age,
                dob = profile['birthdate']
            )
populate_person = PopulatePerson()
populate_person.run()
