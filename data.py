from random import randint
from faker import Faker
fake = Faker()
class BurgerTestData:
    AUTH_EMAIL = fake.email()
    AUTH_NAME = fake.name()
    AUTH_PASSWORD = fake.password(length=randint(6, 10))
    BAD_AUTH_PASSWORD = fake.password(length=randint(4, 5))

    AUTH_EMAIL_CONST = 'ypearson@example.org'
    AUTH_PASSWORD_CONST = '$5^Gy@'
    AUTH_NAME_CONS = "ypearso"


