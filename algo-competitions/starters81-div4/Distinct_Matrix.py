t = int(input())

for _ in range(t):
    n = int(input())
    if n == 2:
        print(-1)
    for i in range(1, n+1):
        if i == 2:
            print("01"+(n-i)*"0")
        else:
            print("1"*(i)+(n-i)*"0")
