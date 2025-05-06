import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.random()
# result = random.choice(card)
random.shuffle(card)

print(f"Random card: {card[0]}")
