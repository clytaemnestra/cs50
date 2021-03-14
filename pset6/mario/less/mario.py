from cs50 import get_int

# asks user for input
while True:
    n = get_int("Height: ")
    if n <= 8 and n >= 1:
        break

for i in range(n):
    for j in range(n - i - 1, 0, -1):
        print(" ", end="")
    for h in range(i):
        print("#", end="")
    print("#")
