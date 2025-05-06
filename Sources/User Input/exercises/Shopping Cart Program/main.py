item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total_price = price * quantity

print(f"Yout have bought {quantity} x {item}/s")
print(f"Your total is: ${total_price}")
