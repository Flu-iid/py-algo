from math import log2


def operations(n: int, k: int):
    if n % k == 0:
        return 0
    while n % 2 == 0 and k % 2 == 0:
        n /= 2
        k /= 2

    k2 = log2(k)
    n2 = log2(n)
    check2_k = int(k2) if k2 == int(k2) else 0
    check2_n = int(n2) if n2 == int(n2) else 0

    if check2_k:
        return check2_k-check2_n
    else:
        return -1


for _ in range(int(input())):
    n, k = map(int, input().split())  # cakes, guests
    print(operations(n, k))
