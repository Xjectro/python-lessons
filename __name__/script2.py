from script1 import *


def favorite_drink(drink):
    print(f"Your favorite drink is {drink}.")


def main():
    print("You are script2")
    favorite_drink("coffee")
    print("Goodbye from script2")


if __name__ == "__main__":
    main()
