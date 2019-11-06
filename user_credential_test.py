import unittest
from user import User

class testUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User("osman","mohamed","4@PO3*")

    def test__init__(self):

        self.assertEqual(self.new_user.first_name,"osman")
        self.assertEqual(self.new_user.last_name,"mohamed")
        self.assertEqual(self.new_user.password,"4@PO3*")


    def save_user(self):


        self.new_user.save_user(self)
        self.assertEqual(len(User.user_list),1)



if __name__ == '__main__':
    unittest.main()        