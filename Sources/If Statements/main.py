age = int(input("Enter your age: "))

if age >= 100:
    print("You are a centenarian")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("You are not born yet")
else:
    print("You are a minor")
