# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "banana", "cherry"]
# fruits = {"apple", "banana", "cherry"}
fruits = ("apple", "banana", "cherry")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits.add("pineapple")
# fruits.remove("banana")
# fruits.pop()

# fruits.index("banana")
# fruits.count("coconut")

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("banana")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# print(fruits.index("cherry"))
# fruits.clear()
# print(fruits.count("apple"))
print(fruits)

# print(fruits[0])
# for fruit in fruits:
#     print(fruit)