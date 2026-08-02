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
