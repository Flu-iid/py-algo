yes, no = "YES", "NO"


def check(b, z, n):
    for i in range(n-1):
        if b[i]+b[i+1] >= z:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    b = [int(i) for i in input().split()]
    b.sort()
    z = b[-1]+b[-2]
    if len(set(b)) < 2:
        print(no)
    elif check(b, z, n):
        print(yes)
    else:
        print(no)
