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
            contacts[name] = {"age": int(age), "email": email, "mob_num": mob_num}
            print(f"Contact name {name} has been created successfully! ")
