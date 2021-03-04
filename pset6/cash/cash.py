from cs50 import get_float

# Get amount of dollars from user
while True:
    dollars = get_float("Change owed: ")
    cents = round(dollars * 100)

if dollars > 0:
    break

counter = 0
change = 0

# Use quarters, while possible
while change + 25 <= cents:
    change = change + 25
    counter += 1

# Use dimes, while possible
while change + 10 <= cents:
    change = change + 10
    counter += 1

# Use nickels, while possible
while change + 5 <= cents:
    change = change + 5
    counter += 1

# Use pennies, while possible
while change + 1 <= cents:
    change = change + 1
    counter += 1

# Print minimum amount of coins
print(counter)
