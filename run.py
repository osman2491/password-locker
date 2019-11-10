#!/usr/bin/env python3.6
import random
import string
from credential import Credential
from user import User

def create_user(fname,lname,password):

        new_user = User(fname,lname,password)
        return new_user
def create_credential(app,app_password):

    new_credential = Credential(app,app_password)

    return new_credential

def save_user_accout(user):

    user.save_user()

def save_credentials(credential):

    credential.save_app()

def app_exist(app):

    return Credential.app_exists(app)

def display_apps():


    return Credential.display_app()

def generate_password():

    generate_password = Credential.gen_password()
    return generate_password

def delete_apps(self):

    return Credential.delete_app(self)


def main():

    print("WELCOME TO PASSWORD LOCKER, 'please enter your name'")

    user_name = input().lower()

    while True:
        print("*"*60)
        print("create app password using this short code: 'mine' = your own password, 'gp' = to generate password")

        password = input()


        if password == 'mine':
            print("Enter your password")
            password = input()
            break

        elif password == 'gp':

            password = generate_password()
            break

        else: print("Enter a valid password")

        



    print(f"welcome {user_name}!")


    while True:
        print("*"*60)
        print("use this short code: 'sc' = to save user credentials, 'dc' = to display your credentials, 'del' = to delete your credentials, exit = to exit the app")

        short_code = input().lower()

        if short_code == 'sc':

            print("*"*60)
            print("Enter your new app name")

            app = input()

            while True:
                print('\n')
                print("Enter your password, use this short code: 'mine' = to enter your password , 'gp' = to generate your password")

                password = input()

                if password == 'mine':

                    print("Enter your password")

                    app_password = input()
                    break
                
                elif password == 'gp':

                    app_password = generate_password()
                    break

                else: print("Enter a valid short code")

            save_credentials(create_credential(app,password))
            
            print(f"new {app} account created!'\n'")
            print (f"password: {app_password}")

        elif short_code == 'dc':
            if app_exist(app):
                print("this are the list of apps that exist ")

                for credential in display_apps():

                    print(f"{credential.app} password : {credential.app_password}")
                    
                else:
                    print("you have no saved apps")

        elif short_code == 'del':

            print("type the app you want to delete")

            app = input()

            print("type the app password")

            app_password = input()

            delete = app.delete_app()

            return delete

        elif short_code == 'exit':

            print("thank you for using password locker")

            break
        else:
            ("please Enter a valid short code")

if __name__ == "__main__":

    main()

