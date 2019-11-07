class User:
    

    user_list = [] 

    def __init__(self,first_name,last_name,password):


        self.first_name = first_name
        self.last_name = last_name
        self.password = password
 
    def save_user(self):


        User.user_list.append(self)

    def delete_user(self):


        User.user_list.remove(self)

    @classmethod
    def find_user_by_first_name(cls,first_name):

        for user in cls.user_list:
            if user.first_name == first_name:
                    return user


    @classmethod
    def user_exist(cls,first_name):

        for user in cls.user_list:

            if user.first_name == first_name:

                return True


    

        
