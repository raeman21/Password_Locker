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

    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
        the contact list
        '''
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    def tearDown(self):
        '''
        tearDown method that does cleanup after each test case has run.
        '''
        Contact.contact_list = []

    def test_save_multiple_contact(self):
        '''
        test_save_multiple to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", "3983739873", "test@mail.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

    def test_delete_contact(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_contact.save_contact()
        test_contact.save_contact()

        self.new_contact.delete_contact()

        self.assertEqual(len(Contact.contact_list), 1)

    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", "3983739873", "test@mail.com")
        test_contact.save_contact()

        found_contact = Contact.find_by_number("3983739873")

        self.assertEqual(found_contact.email, test_contact.email)


if __name__ == '__main__':
    unittest.main()
