for _ in range(int(input())):
    l, r = map(int, input().split())
    count = 0
    for a in range(l, r+1):
        for b in range(a, r+1):
            if a ^ b == a+b:
                count += 1
    print(count)
