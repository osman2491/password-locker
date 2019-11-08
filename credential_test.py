import unittest 
from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):

        self.new_credentail = Credential("facebook","PY232")

    def test__init__(self):

        self.assertEqual(self.new_credentail.app,"facebook")
        self.assertEqual(self.new_credentail.password,"PY232")

    def test_save_app(self):

        self.new_credentail.save_app()

        self.assertEqual(len(Credential.app_details),1)

    

if __name__ == "__main__":
    unittest.main()