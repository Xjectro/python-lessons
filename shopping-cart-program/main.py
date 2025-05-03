foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy (q to quit): ")
    if food.lower() == "q":
        break
    price = float(input(f"Enter price for {food}: $"))
    foods.append(food)
    prices.append(price)
    total += price
    print(f"Added {food} for ${price:.2f}. Total so far: ${total:.2f}")

print("Shopping cart items:")
for food, price in zip(foods, prices):
    print(f"Item: {food}, Price: ${price:.2f}")

print(f"Total: ${total:.2f}")
