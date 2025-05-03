import helper

class Credentials:
    name='NikolaIvanov21'
    email='nikolaivanov2159@yandex.ru'
    password='NikolaPassword'

    random_name = helper.UserGenerator().generate_name()
    random_email = helper.UserGenerator().generate_email()
    random_password = helper.PasswordGenerator().generate_password()

    empty_name = helper.UserGenerator().generate_empty_name()
    wrong_password = helper.PasswordGenerator().generate_wrong_password()

