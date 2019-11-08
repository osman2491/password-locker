import unittest 
from credential import Credential

class TestCredential(unittest.TestCase):

    def tearDown(self):

        Credential.app_details = []

    def setUp(self):

        self.new_credentail = Credential("facebook","PY232")

    def test__init__(self):

        self.assertEqual(self.new_credentail.app,"facebook")
        self.assertEqual(self.new_credentail.password,"PY232")

    def test_save_app(self):

        self.new_credentail.save_app()

        self.assertEqual(len(Credential.app_details),1)

    def test_delete_app(self):

        self.new_credentail.save_app()
        test_credential = Credential("facebook","PY6723")
        test_credential.save_app()


        self.new_credentail.delete_app()
        self.assertEqual(len(Credential.app_details),1)

    def test_find_by_app_name(self):

        self.new_credentail.save_app()
        test_credential = Credential("facebook","PY232")
        test_credential.save_app()

        found_app =  Credential.find_app("facebook")

        self.assertTrue(found_app,test_credential.app)  

    

if __name__ == "__main__":
    unittest.main()