t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()

    ideal_a = range(n)

    operations = 0
    for i, e in enumerate(a):
        operations += abs(ideal_a[i] - e)

    print(operations)
