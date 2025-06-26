def answer(n, l: list):
    l.sort()
    i = 0
    result = []
    while i < len(l):
        if l[i] == 1 and n in l:
            return [1, n]
        elif n % l[i] == 0:
            n /= l[i]
            result.append(l[i])
        i += 1

    return result[-2], result[-1]


for _ in range(int(input())):
    n = int(input()) - 2
    l = [int(i) for i in input().split()]
    print(*answer(n, l))
