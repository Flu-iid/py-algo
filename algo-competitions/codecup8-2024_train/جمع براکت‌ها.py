def func(n: int, x: float):
    a = int(x)  # float number a.b
    b = 1 - (x-a)  # complement b
    if b == 1:
        return n * a
    c = int(b * n)  # 1 index before change
    return c * a + (n - c) * (a + 1) - 1
# why -1 :D


for _ in range(int(input())):
    n = int(input())
    x = float(input())
    print(func(n, x))
