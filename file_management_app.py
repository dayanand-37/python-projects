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
