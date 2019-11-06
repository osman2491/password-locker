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



if __name__ == '__main__':
    unittest.main()


