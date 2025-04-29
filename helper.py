import random

from faker import Faker


symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


class UserGenerator:
    fake = Faker()

    @staticmethod
    def generate_name():
        return UserGenerator.fake.name()

    @staticmethod
    def generate_empty_name():
        return ""

    @staticmethod
    def generate_email():
        return UserGenerator.fake.company_email()


class PasswordGenerator:
    
    @staticmethod
    def generate_password():
        lenght_password = random.randint(6, 15)
        password = ''.join([random.choice(symbols) for _ in range(lenght_password)])
        return password

    @staticmethod
    def generate_wrong_password():
        lenght_password = random.randint(1, 5)
        password = ''.join([random.choice(symbols) for _ in range(lenght_password)])
        return password
    
