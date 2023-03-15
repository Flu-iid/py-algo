t = int(input())


def check(c0, c1):
    if c0 == c1:
        return 0
    if n % 2 != 0:
        return -1
    tmp = int(abs(c0-c1)/2)
    if tmp % 2 == 0:
        return int(tmp/2)
    else:
        if c0 > c1:
            if c1 > 0:
                return tmp // 2 + 1
            else:
                return -1
        else:
            if c0 > 0 and c1 > 2:
                return tmp // 2 + 2
            else:
                return -1


for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c0, c1 = a.count(0), a.count(1)
    print(check(c0, c1))
