def hello(greeting, title, first, last):
    return f"{greeting} {title}{first} {last}"


result = hello(title="Mr.", last="Smith", first="John", greeting="Hello")

# print(result)

# print("1", "2", "3", "4", "5", "6", sep="-")


def get_phone(country, area, first, last):
    return f"+{country} ({area}) {first}-{last}"


phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)
