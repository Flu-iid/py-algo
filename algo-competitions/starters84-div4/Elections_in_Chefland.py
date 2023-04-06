for _ in range(int(input())):
    n, x = map(int, input().split())
    l = [int(i) for i in input().split()]
    count = 0
    for i in l:
        if i >= x:
            count += 1
    print(count)
