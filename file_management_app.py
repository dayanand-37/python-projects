import os


def create_file(filename):
    try:
        with open(filename, "x") as f:
            print(f"file {filename} created successfully!")

    except FileExistsError:
        print(f"file {filename} already exists!")

    except Exception as e:
        print("An error occured!")


def view_all_files():
    files = os.listdir()
    if not files:
        print("file not found!")
    else:
        print("files in directory!")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} is deleted successfully!")

    except FileNotFoundError:
        print("file not found!")

    except Exception as e:
        print("An error occured")


def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"The content of the '{filename}' : \n{content}")

    except FileNotFoundError:
        print(f"{filename} does not exists!")

    except Exception as e:
        print("An error occured!")


def edit_file(filename):
    try:
        with open(filename, "a") as f:
            content = input("Enter data to add = ")
            f.write(content + "\n")
            print(f"Content is added successfully in the file {filename}")

    except FileNotFoundError:
        print(f"{filename} does not exists!")

    except Exception as e:
        print("An error occured!")


def main():
    while True:
        print("File management App")
        print("1: To create a file")
        print("2: To view all files")
        print("3: To delete a file")
        print("4: To read a file")
        print("5: To edit a file a file")
        print("6: To exit the app")

        choice = input("Enter your choice between 1-6 ")

        if choice == "1":
            filename = input("Enter the file-name to create = ")
            create_file(filename)

        elif choice == "2":
            view_all_files()

        elif choice == "3":
            filename = input("Enter the name of the file you want to delete = ")
            delete_file(filename)

        elif choice == "4":
            filename = input("Enter the name of the file you want to read = ")
            read_file(filename)

        elif choice == "5":
            filename = input("Enter the name of the file you want to edit = ")

        elif choice == "6":
            print("Closing the app....")
            break

        else:
            print("Error! 'Enter your choice in the given range'")


if __name__ == "__main__":
    main()
