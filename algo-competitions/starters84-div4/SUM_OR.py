from math import factorial
for _ in range(int(input())):
    n = int(input())
    b = bin(n)[2:]
    if b.count("1") < 3:
        print(0)
    else:
        print(factorial(len(b.strip("0"))) % (10**9+7))
