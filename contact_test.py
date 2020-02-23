import unittest
from contact import Contact


class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours

    Args:
        unittest.TestCase: Testcase class that helps in creating test cases

    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact(
            "Irene", "Adler", "98378973", "iadler@gmail.com")  # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name, "Irene")
        self.assertEqual(self.new_contact.last_name, "Adler")
        self.assertEqual(self.new_contact.phone_number, "98378973")
        self.assertEqual(self.new_contact.email, "iadler@gmail.com")

    if __name__ == '__main__':
        unittest.main()
