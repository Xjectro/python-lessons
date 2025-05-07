import os

file_path = "c:\\Users\\{username}\\Documents\\GitHub\\python-lessons\\Sources\\File Detection\\test.txt"

if os.path.exists(file_path):
    print(f"The file {file_path} exists.")

    if os.path.isfile(file_path):
        print(f"{file_path} is a file.")
    elif os.path.isdir(file_path):
        print(f"{file_path} is a directory.")
else:
    print(f"The file {file_path} does not exist.")
