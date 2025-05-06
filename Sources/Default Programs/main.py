def net_price(list_price, discount=0.10, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


result = net_price(100, 0.2, 0.04)
print(f"The net price is: ${result:.2f}")
