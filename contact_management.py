from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")

db = client["phonebook"]

contacts = db["contacts"]



def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.insert_one(contact)
    print("✅ Contact added successfully!")

def view_contacts():
    print("\n📒 All Contacts:")
    for contact in contacts.find():
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    name = input("Enter name to search: ")
    result = contacts.find_one({"name": name})
    if result:
        print(f"👤 Found: Name: {result['name']}, Phone: {result['phone']}, Email: {result['email']}")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    result = contacts.delete_one({"name": name})
    if result.deleted_count > 0:
        print("🗑️ Contact deleted.")
    else:
        print("❌ No such contact found.")

def update_contact():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")
    result = contacts.update_one({"name": name}, {"$set": {"phone": new_phone}})
    if result.modified_count > 0:
        print("🔁 Contact updated.")
    else:
        print("❌ Update failed. Contact may not exist.")

while True:
    print("\n📱 PHONE BOOK MENU")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Try again.")
        break