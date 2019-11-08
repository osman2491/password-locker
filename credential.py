import random
import string
class Credential:

    app_details = []

    def __init__(self,app,password):

        self.app = app
        self.password = password

    def save_app(self):

        self.app_details.append(self)

    def delete_app(self):

        self.app_details.remove(self)

    @classmethod
    def find_app(cls,app):


        for Credential in cls.app_details:

            if Credential.app == app:

                return True

    @classmethod
    def app_exists(cls,app):

        for Credential in cls.app_details:
            if Credential.app == app:
                return True

        return False


    @classmethod
    def gen_password(self):


        char = string.ascii_uppercase + string.ascii_lowercase
        gen_password = ''.join(random.choice(char) for i in range(0, 9))
        return gen_password

    @classmethod
    def display_app(cls,app):

        return cls.app_details