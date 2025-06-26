a, b = map(int, input().split())

# a is mean
# b is median

p, q, l = 0, 0, 0

if a == b:
    p = a - 1
    q = a + 1
    print(2)
    print(p, q)
else:
    q = b
    p = 3 * a - b
    print(3)
    print(p, q, 0)
