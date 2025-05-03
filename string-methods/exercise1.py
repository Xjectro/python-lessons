# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Username must be no more than 12 characters.")
elif not username.find(" ") == -1   :
    print("Username must not contain spaces.")
elif not username.isalpha():
    print("Username must not contain digits.")
else:
    print(f"Hello {username}!")