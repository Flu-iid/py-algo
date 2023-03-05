t = int(input())


def rc(c):
    """
    reverse char case
    """
    if c == c.lower():
        return c.upper()
    else:
        return c


def score(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    needed_k = 0
    for key in d:
        pass


for i in range(t):
    n, k = map(int, input().split(" "))
    s = input()
