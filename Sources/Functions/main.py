persons = (
    {"Name": "Alice", "Age": 25},
    {"Name": "Bob", "Age": 30},
    {"Name": "Charlie", "Age": 35},
)


def happy_birthday(name, age):  # we dont need argument names in the function definition
    print("Happy Birthday to you!", end="\n \u200b \n")
    print("Happy Birthday dear", name, end="\n \u200b \n")
    print("You are now", age, "years old!", end="\n \u200b \n")


for person in persons:
    happy_birthday(person["Name"], person["Age"])
