for _ in range(int(input())):
    x, y = map(int, input().split())
    i = 0
    while y < x:
        i += 1
        y += i
    print(i)
