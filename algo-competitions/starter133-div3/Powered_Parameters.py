t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    count = 0
    max_a = max(a)
    for i, e1 in enumerate(a):
        for j, e2 in enumerate(a):
            if e1 ** (j + 1) > max_a:
                break
            if e1 == 1:
                count += n
                break
            if e1 ** (j + 1) <= e2:
                count += 1
    print(count)
