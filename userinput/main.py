# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = input("How old are you?: ")

age = int(age) # Convert age to integer
# or age = int(input("How old are you?: ")) # Convert age to integer in one line
age += 1 # Increment age by 1


print(f"Hello {name}")
print(f"HAPPY BIRTHDAY")
print(f"You are {age} years old")