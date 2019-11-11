import unittest 
from user import User 

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def tearDown(self):

        '''
        tearDown method that does clean up after each test case has run.
        '''
            
        User.user_list = []


    def setUp(self):

        '''
        Set up method to run before each test cases.
        '''
        
        self.new_user = User("osman","mohamed","P@#97")


    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"osman")
        self.assertEqual(self.new_user.last_name,"mohamed")
        self.assertEqual(self.new_user.password,"P@#97")


    def test_save_user(self):

        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)


    def test_delete_user(self):

        '''
        test_delete_user to test if we can remove a user from our user list
        '''
            
        self.new_user.save_user()
        test_user = User("osman","mohamed","P@#97") 
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_first_name(self):

        '''
        test to check if we can find a user by phone firstname and display information
        '''


        self.new_user.save_user()
        test_user = User("osman","mohamed","P@#97")
        test_user.save_user()

        find_user = User.find_user_by_first_name("osman")

        self.assertEqual(find_user.password,test_user.password)

    def test_user_exist(self):

        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("osman","mohamed","P@#97")
        test_user.save_user()

        user_exists = User.user_exist("osman")

        self.assertTrue(user_exists)

    def test_display_user(self):

        '''
        method that returns a list of all user saved
        '''


        self.assertEqual(User.display_users(),User.user_list)





if __name__ == '__main__':
    unittest.main()


