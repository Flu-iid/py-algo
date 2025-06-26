# https://quera.org/problemset/281769

n, k = map(int, input().split())

zarfiat = n//2 + n%2
def pair(k):
    print((k - zarfiat) * 2)

if k >= n:
    print(n-1)
elif k <= zarfiat:
    print(0)
else:
    print(k*2-n-1-2*(n%2))