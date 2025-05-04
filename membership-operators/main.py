word = "APPLE"

letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f"Good job! The letter '{letter}' is in the word.")
# else:
#     print(f"Sorry, the letter '{letter}' is not in the word.")

if letter not in word:
    print(f"Sorry, the letter '{letter}' is not in the word.")
else:
    print(f"Good job! The letter '{letter}' is in the word.")
