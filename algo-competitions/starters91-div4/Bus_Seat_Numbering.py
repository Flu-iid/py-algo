t = int(input())
for _ in range(t):
    n = int(input())
    if n > 15:
        print("Upper ", end="")
    else:
        print("Lower ", end="")
    if n < 11 or n > 15 and n < 26:
        print("Double")
    else:
        print("Single")
