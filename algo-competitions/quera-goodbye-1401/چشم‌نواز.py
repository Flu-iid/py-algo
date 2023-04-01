t = int(input())

# first_floor = [4,3,2,2,2,...]
# if 2 floors *2


def choose(n, m):
    if n == 1 and m != 1:
        return 4*3**(m-1)
    elif m == 1 and n != 1:
        return 4*3**(n-1)
    elif n == 2 and m != 1:
        return 4*3*2*2**(m-2)
    elif m == 2 and n != 1:
        return 4*3*2*2**(n-2)
    elif n >= 3 and m >= 3:
        return (4*3)*2**(n-1)*2**(m-2)
    return 4


for _ in range(t):
    n, m = map(int, input().split())
    print(choose(n, m) % (10**9+7))
