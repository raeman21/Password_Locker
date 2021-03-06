#!/usr/bin/env python3.6
from contact import Contact

def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(contact):
    '''
    Function to save contacts
    '''
    return contact.save_contact()

def del_contact(contact):
    '''
    Function to delete a contact
    '''
    return contact.delete_contact()

def find_contact(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Contact.find_by_number(number)

def check_existing_contacts(number):
    '''
    Function that checks if a contact exists with that number and return a Boolean
    '''
    returnContact.contact_exist(number)

def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_contacts()

def copy_email():
    '''
    Function that copies email to clipboard
    '''
    return Contact.copy_email()

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc - find a contact, ex - exit the contact list, lc - delete contact, cp - copy contact email ")

        short_code = input().lower()
        
        if short_code == 'cc':
            print("New Contact")
            print("-" * 10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            save_contacts(create_contact(f_name,l_name,p_number,e_address))
            print ('\n')
            print (f"New contact {f_name} {l_name} created")
            print ('\n')
        elif short_code == 'dc':

            if display_contacts():
                print("Here is a list of all your contacts")
                print ('\n')

                for contact in display_contacts():
                    print(f"{contact.first_name} {contact.phone_number} {contact.email}")
                    print ('\n')
            else:
                    print ('\n')
                    print ("You don't seem to have any contacts saved yet")
                    print ('\n')
            
        elif short_code == 'fc':
            
            print ("enter the number you want to search for")

            search_number = input()

            if check_existing_contacts(search_number):
                search_contact = find_contact (search_number)
                print (f"{search_contact.first_name} {search_contact.last_name}")
                print ('-' * 20)
                print (f"Phone number ....... {search_contact.phone_number}")
                print (f"Email address ....... {search_contact.email}")
            
            else:
                print ("That contact does not exist")

        elif short_code == "ex":

            print ("I really didn't get that. Please use the short codes")

        # elif short_code == "lc":
        #     print ("Which contact would you like to delete?")

        #     for contact in display_contacts():
        #             print(f"{contact.first_name} {contact.phone_number} {contact.email}")
        #             print ('\n')

        #             delete_contact = input()

        #             if input(f_name) == contact.f_name:
        #                 print (f"Old contact {f_name.delete_contact} {l_name.delete_contact} deleted")

        #             else:
        #                 print ("That contact does not exist")

if __name__ == '__main__':

    main()