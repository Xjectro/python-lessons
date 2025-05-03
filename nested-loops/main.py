# nested loops = A loop within another loop (outer, inner)
#                outer loop:
#                    inner loop:

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol: ")

for row in range(rows):
    for column in range(columns):
        print(symbol, end="")
    print()
