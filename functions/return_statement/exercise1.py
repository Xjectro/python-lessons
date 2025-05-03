def create_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"

name = create_name("john", "doe")

print(name)