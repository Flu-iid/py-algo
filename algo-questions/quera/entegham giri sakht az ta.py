n = int(input())


def odd_n(n):
    return 2**(n//2+1)*(n//2+1)*2


def even_n(n):
    return 3**(n//2)


if n == 1:
    print(4)
elif n % 2 == 0:
    print(even_n(n)*2)
else:
    print(odd_n(n)*2)
