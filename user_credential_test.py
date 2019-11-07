import unittest 
from user import User 

class TestContact(unittest.TestCase):


    def tearDown(self):
            
            User.user_list = []


    def setUp(self):
        
        self.new_user = User("osman","mohamed","P@#97")


    def test_init(self):

        self.assertEqual(self.new_user.first_name,"osman")
        self.assertEqual(self.new_user.last_name,"mohamed")
        self.assertEqual(self.new_user.password,"P@#97")


    def test_save_user(self):
        
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)


    def test_delete_user(self):
            
            self.new_user.save_user()
            test_user = User("osman","mohamed","P@#97") 
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)

    def test_find_user_by_first_name(self):


        self.new_user.save_user()
        test_user = User("osman","mohamed","P@#97")
        test_user.save_user()

        find_user = User.find_user_by_first_name("osman")

        self.assertEqual(find_user.password,test_user.password)

    def test_user_exist(self):

        self.new_user.save_user()
        test_user = User("osman","mohamed","P@#97")
        test_user.save_user()

        user_exists = User.user_exist("osman")

        self.assertTrue(user_exists)

    def test_display_user(self):


        self.assertEqual(User.display_users(),User.user_list)





if __name__ == '__main__':
    unittest.main()


