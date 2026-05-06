#6.	Create a contact book where users can store, search, update, and delete contacts. 
contacts = {}

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Exit")
    ch = input("Enter choice: ") or "5"

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif ch == "2":
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))

    elif ch == "3":
        name = input("Update name: ")
        if name in contacts:
            contacts[name] = input("New phone: ")

    elif ch == "4":
        name = input("Delete name: ")
        contacts.pop(name, None)

    else:
        break