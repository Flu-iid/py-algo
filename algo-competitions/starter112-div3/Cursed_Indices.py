for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    curse_count = 0
    array_sum = a[0]
    for i in range(1, n):
        if a[i] <= array_sum:
            curse_count += 1
        array_sum += a[i]
    print(curse_count)
    print(" ".join(map(str, a)))
