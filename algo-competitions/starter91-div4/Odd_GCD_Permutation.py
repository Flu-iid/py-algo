for _ in range(int(input())):
    n = int(input())
    if not n % 2:
        for i in range(n, 0, -1):
            print(i, end=" ")
        print()
    else:
        print(-1)
