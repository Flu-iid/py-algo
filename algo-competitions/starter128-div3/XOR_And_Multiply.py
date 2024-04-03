t = int(input())
for _ in range(t):
    x = int(input())
    b = x
    while True:
        mxor = x & b
        mand = x ^ b
        if mxor % x == 0 and mand % x == 0 and mxor > 0 and mand > 0:
            break
        else:
            b += 2 * x

    print(x, b)
