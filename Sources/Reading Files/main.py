import json
import csv

base_path = "c:/Users/{username}/Documents/GitHub/python-lessons/Sources/Reading Files/"

txt_file_path = base_path + "input.txt"
json_file_path = base_path + "input.json"
csv_file_path = base_path + "input.csv"


def read_file(file_path, type):
    try:
        with open(file_path, mode="r") as file:
            if type == "txt":
                content = file.read()
            elif type == "json":
                content = json.load(file)
            elif type == "csv":
                content = csv.reader(file)
            else:
                raise ValueError("Unsupported file type")
            return content
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except PermissionError:
        print(f"Permission denied to read file {file_path}.")
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")


content = read_file(txt_file_path, "txt")
print(f"File {txt_file_path} read successfully.")
print(f"Content: {content}")
