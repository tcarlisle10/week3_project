import re
from helper import clear


def main():
    while True:
        contacts_list = read_contacts()
        action = input('''
Options
-----------------------
1 - Add a new contact
2 - Remove a contact
3 - View all contacts
4 - Edit contact
5 - Search for a contact
6 - Quit
''')
        if action == '1':
            add_contact(contacts_list) 
        elif action == '2':
            remove_contact(contacts_list) 
        elif action == '3':
            view(contacts_list) 
        elif action == '4':
            update_contact(contacts_list) 
        elif action == '5':
            search_contact(contacts_list) 
        elif action == '6':
            print("Thanks for using this app!")
            break


def write_contacts(contacts): 
    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            file.write(f"{contact['Name']}-:-{contact['Email']}-:-{contact['Phone']}\n")

def read_contacts(): 
    contacts_list = []
    with open('contacts_list.txt', 'r') as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            contacts_list.append({'Name': data.group(1), 'Email': data.group(2), 'Phone': data.group(3).strip()})
    return contacts_list



def add_contact(contacts):
    clear()
    name = input("What is your name? ")
    email = input("What is your email? ")
    phone = input("what is your phone number? ")
    contacts.append({'Name': name, 'Email': email, 'Phone': phone})
    write_contacts(contacts)


def view(contacts):
    clear()
    print("Shows List")
    print('-----------------------')
    for idx, contact in enumerate(contacts):
        vowels = ['a', 'e', 'i', 'o', 'u']
        a_or_an = 'an' if contact['Title'][0].lower() in vowels else 'a'
        print(f"{idx + 1}.) {contact['Title']} is {a_or_an} {contact['Email']} {contact['Phone']}")


def remove_contact(contacts):
    view(contacts)
    option = int(input("\n\nChoose a number for the contacts you'd like to remove: "))
    contacts = contacts.pop(option - 1)
    print(f"\n{contacts['Name']} was successfully removed!")
    write_contacts(contacts)


def update_contact(contacts):
    view(contacts)
    option = int(input("\n\nChoose a number for the contacts you'd like to update: "))

    email = input("What is the new phone number? ")
    phone = input("What is the new phone number? ")

    customer_update = (option, email, phone)

    return (f"{customer_update} successfully update")

def search_contact(contacts):
    view(contacts)
    option = int(input("\n\nChoose a number for the contacts you'd like to update: "))

    return option