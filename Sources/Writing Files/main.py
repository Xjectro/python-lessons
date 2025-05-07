from types import SimpleNamespace
import json
import csv

base_path = "c:/Users/{username}/Documents/GitHub/python-lessons/Sources/Writing Files/"

txt_file = SimpleNamespace(
    file_path=base_path + "output.txt",
    content="Hello, Spongebob!",
)

json_file = SimpleNamespace(
    file_path=base_path + "output.json",
    content={"name": "Spongebob", "age": 20, "city": "Bikini Bottom"},
)

csv_file = SimpleNamespace(
    file_path=base_path + "output.csv",
    content=[
        ["Name", "Age", "City"],
        ["Spongebob", 20, "Bikini Bottom"],
        ["Patrick", 21, "Bikini Bottom"],
        ["Squidward", 22, "Bikini Bottom"],
    ],
)

try:
    with open(file=json_file.file_path, mode="w") as file:
        json.dump(json_file.content, file, indent=4)
        print(f"File {json_file.file_path} created successfully.")
        print(f"Content: {json_file.content}")
except FileExistsError:
    print(f"File {json_file.file_path} already exists.")
except FileNotFoundError:
    print(f"File {json_file.file_path} not found.")
except Exception as e:
    print(f"Error creating file {json_file.file_path}: {e}")


try:
    with open(file=csv_file.file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in csv_file.content:
            writer.writerow(row)
        print(f"File {csv_file.file_path} created successfully.")
        print(f"Content: {csv_file.content}")
except FileExistsError:
    print(f"File {csv_file.file_path} already exists.")
except FileNotFoundError:
    print(f"File {csv_file.file_path} not found.")
except Exception as e:
    print(f"Error creating file {csv_file.file_path}: {e}")


try:
    with open(file=txt_file.file_path, mode="w") as file:
        file.write(txt_file.content)
        print(f"File {txt_file.file_path} created successfully.")
        print(f"Content: {txt_file.content}")
except FileExistsError:
    print(f"File {txt_file.file_path} already exists.")
except FileNotFoundError:
    print(f"File {txt_file.file_path} not found.")
except Exception as e:
    print(f"Error creating file {txt_file.file_path}: {e}")
