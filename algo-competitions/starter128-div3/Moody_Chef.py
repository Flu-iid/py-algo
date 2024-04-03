t = int(input())


def score(n: int, l, r):
    if l <= n <= r:
        return 1
    return -1


for _ in range(t):
    n, l, r = map(int, input().split())
    a = input().split()
    current, min, max = 0, 0, 0
    for i in a:
        current += score(int(i), l, r)
        if current > max:
            max = current
        if current < min:
            min = current
    print(max, min)
