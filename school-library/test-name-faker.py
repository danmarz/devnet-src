from faker import Faker
fake = Faker()


print('My name is {}.'.format(fake.name()))
