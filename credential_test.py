import unittest 
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''



    def tearDown(self):

        '''
        tearDown method that does clean up after each test case has run.
        
        '''

        Credential.app_details = []

    def setUp(self):
    
        '''
        Set up method to run before each test cases.
        '''



        self.new_credentail = Credential("app","password")

    def test__init__(self):

        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentail.app,"app")
        self.assertEqual(self.new_credentail.password,"password")

    def test_save_app(self):

        '''
        test_save_app test case to test if the credential object is saved into
         the credential list
        '''


        self.new_credentail.save_app()

        self.assertEqual(len(Credential.app_details),1)

    def test_delete_app(self):

        '''
        test_delete_credentials to test if we can remove a credential from our credential list
        
        '''

        self.new_credentail.save_app()
        test_credential = Credential("facebook","PY6723")
        test_credential.save_app()


        self.new_credentail.delete_app()
        self.assertEqual(len(Credential.app_details),1)

    def test_find_by_app_name(self):

        '''
        test to check if we can find a credential by app name and display information
        
        '''

        self.new_credentail.save_app()
        test_credential = Credential("facebook","PY232")
        test_credential.save_app()

        found_app =  Credential.find_app("facebook")

        self.assertTrue(found_app,test_credential.app)  

    def test_app_exist(self):


        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credentail.save_app()
        test_credential = Credential("facebook","PY232")
        test_credential.save_app()

        apps_exist = Credential.find_app("facebook")

        self.assertTrue(apps_exist)

    def test_display_app(self):


        '''
        method that returns a list of all app details saved
        '''

        self.assertEqual(Credential.display_app,Credential.app_details)

        

if __name__ == "__main__":
    unittest.main()