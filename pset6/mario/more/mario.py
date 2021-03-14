from cs50 import get_int

# asks user for input
while True:
    n = get_int("Height: ")
    if n <= 8 and n >= 1:
        break

for i in range(n):
    for j in range(1, n - i):
        print(" ", end="")
    for m in range(n - i, n + 1):
        print("#", end="")
    print("  ", end="")    
    for h in range(n - i, n + 1):
        print("#", end="")
    print()
 
