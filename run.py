#!/usr/bin/env python3.6
import random
import string
from credential import Credential
from user import User

def create_user(fname,lname,password):

        new_user = User(fname,lname,password)
        return new_user
def create_credential(app,password):

    new_credential = Credential(app,password)

    return new_credential

def save_user_accout(user):

    user.save_user()

def save_credentials(credential):

    credential.save_app()

def check_existing_users(details):

    details.user_exist(details)

def display_credentials():


    return Credential.display_app


# def main():

#     print("WELCOME TO PASSWORD LOCKER")

