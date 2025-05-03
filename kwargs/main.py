def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


# print(add(1, 2, 3))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")


# display_name("Spongebob", "Squarepants")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# print_address(street="123 Fake St.", city="Detroit", state="MI", zip="41050", apt="A5")


def shipping_label(*args, **kwargs):
    display_name(*args)
    print("")
    print_address(**kwargs)


shipping_label(
    "Dr.",
    "Xjectro",
    street="123 Fake St.",
    city="Detroit",
    state="MI",
    zip="41050",
    apt="A5",
)
