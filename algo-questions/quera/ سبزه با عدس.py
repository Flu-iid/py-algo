# https://quera.org/problemset/281769

# 2 <= n <= 100, 1 <= k <= n

# 1

# n, k = map(int, input().split())

# zarfiat = n//2 + n%2
# def pair(k):
#     print((k - zarfiat) * 2)

# if k == n:
#     print(n-1)
# elif k <= zarfiat:
#     print(0)
# else:
#     print(k*2-n-1-2*(n%2))

# 2

from math import ceil

n, k = map(int, input().split())

zarfiat = ceil(n / 2)

def pairs(n, k, z):
    """get number of pairs next to eachotehr according to z(zarfiatD)"""
    # depend on number of n that if its even or odd, placing k will differ:
    ## odd
    # [III-I] best placing for lowest pairs in n=5, k=4, z=3
    # even
    # [I-I-II] best placing for lowest pairs in n=6, k=4, z=3
    # for even we place 1 at the end, and threat rest like an odd placing

    if k == 1 or k <= z:
        return 0
    elif not n%2: #even
        return pairs(n-1, k-1, z) + 1
    else:    
        return (k-z)*2

print(pairs(n, k, zarfiat))
















