import random
import string
class Credential:

    app_details = []

    def __init__(self,app,app_password):

        self.app = app
        self.password = app_password

    def save_app(self):

        '''
        save_app method saves credential objects into app_details
        '''

        self.app_details.append(self)

    def delete_app(self):

        '''
        delete_app method deletes a saved credential from the app_details
        '''

        self.app_details.remove()

    @classmethod
    def find_app(cls,app):

        '''
        Method that takes in a app name and returns a credential that matches that credential.

        Args:
            credential: app name to search for
        Returns :
            app details of person that matches the credential.
        '''


        for Credential in cls.app_details:

            if Credential.app == app:

                return True
        

    @classmethod
    def app_exists(cls,app):

        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''

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
    def display_app(cls):

        '''
        method that returns the app details
        '''

        return cls.app_details