contacts = {}

while True:
    print("\n Contact book app")
    print("1: To Create contact: ")
    print("2: To View contact: ")
    print("3: To Update contact: ")
    print("4: To Delete contact: ")
    print("5: To Search contact: ")
    print("6: To Count contacts: ")
    print("7: To Exit: ")

    choice = input("Enter your choice(1-6): ")

    if choice == "1":
        name = input("Enter the name: ")
        if name in contacts:
            print(f"Contact name {name} already exists! ")
        else:
            age = input("Enter the age: ")
            email = input("Enter the Email Address: ")
            mob_num = input("Enter the mobile number: ")
            contacts[name] = {"age": int(age), "email": email, "mobile_number": mob_num}
            print(f"Contact name {name} has been created successfully! ")

    elif choice == "2":
        name = input("Enter the name of contact you want to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f"name:{name} age:{age} mobile_number:{mob_num} email:{email}")
        else:
            print(f"contact name {name} not found!")

    elif choice == "3":
        name = input("Enter the name of contact you want to update: ")
        if name in contacts:
            age = input("Enter the updated age: ")
            email = input("Enter the updated Email Address: ")
            mob_num = input("Enter the updated mobile number: ")
            contacts[name] = {"age": int(age), "email": email, "mobile_number": mob_num}

        else:
            print(f"contact name {name} not found!")
