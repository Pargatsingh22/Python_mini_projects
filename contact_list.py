import os

FILENAME = "contacts.txt"

def read_contacts():
    if not os.path.exists(FILENAME):
        return []
    
    with open(FILENAME, 'r') as file:
        contacts = [line.strip() for line in file]
    return contacts

def write_contacts(contacts):
    with open(FILENAME, 'w') as file:
        for contact in contacts:
            file.write(f"{contact}\n")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact number: ")
    contact = f"{name} - {phone}"
    contacts.append(contact)
    write_contacts(contacts)
    print(f"Contact '{name}' added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact}")

def delete_contact():
    view_contacts()
    try:
        contact_index = int(input("Enter contact number to delete: "))
        if 1 <= contact_index <= len(contacts):
            removed_contact = contacts.pop(contact_index - 1)
            write_contacts(contacts)
            print(f"Contact '{removed_contact}' deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    global contacts
    contacts = read_contacts()

    while True:
        print("Options: [1] View Contacts  [2] Add Contact  [3] Delete Contact  [4] Exit")
        option = input("Select an option: ")

        if option == '1':
            view_contacts()
        elif option == '2':
            add_contact()
        elif option == '3':
            delete_contact()
        elif option == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
