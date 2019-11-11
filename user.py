class User:
    

    user_list = [] 

    def __init__(self,first_name,last_name,password):

        '''
        test_init test case to test if the object is initialized properly
        '''


        self.first_name = first_name
        self.last_name = last_name
        self.password = password
 
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''


        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''


        User.user_list.remove(self)

    @classmethod
    def find_user_by_first_name(cls,first_name):

        '''
        Method that takes in firstname and returns a user that matches that firstname.

        Args:
            user:firstname to search for
        Returns :
            user of person that matches the firstname.
        '''

        for user in cls.user_list:
            if user.first_name == first_name:
                    return user


    @classmethod
    def user_exist(cls,first_name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            user: firstname to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''

        for user in cls.user_list:

            if user.first_name == first_name:

                return True


    @classmethod
    def display_users(cls,):

        '''
        method that returns the user list
        '''

        return cls.user_list

        
