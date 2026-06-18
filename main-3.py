contacts = []

while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts.append({"name": name, "phone": phone})

    elif choice == "2":
        for c in contacts:
            print(c["name"], "-", c["phone"])

    elif choice == "3":
        name = input("Search name: ")
        found = False
        for c in contacts:
            if c["name"].lower() == name.lower():
                print(c["name"], "-", c["phone"])
                found = True
        if not found:
            print("Not found")

    elif choice == "4":
        name = input("Delete name: ")
        contacts = [c for c in contacts if c["name"].lower() != name.lower()]
        print("Deleted")

    elif choice == "5":
        break