from types import SimpleNamespace
import json
import csv

base_path = "Assets/"

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


def write_file(file_path, content, type):
    try:
        with open(file_path, mode="w") as file:
            if type == "txt":
                file.write(content)
            elif type == "json":
                json.dump(content, file, indent=4)
            elif type == "csv":
                writer = csv.writer(file)
                for row in content:
                    writer.writerow(row)
            else:
                raise ValueError("Unsupported file type")
            print(f"File {file_path} created successfully.")
            print(f"Content: {content}")
    except FileExistsError:
        print(f"File {file_path} already exists.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"Error creating file {file_path}: {e}")


write_file(json_file.file_path, json_file.content, "json")
write_file(csv_file.file_path, csv_file.content, "csv")
write_file(txt_file.file_path, txt_file.content, "txt")
