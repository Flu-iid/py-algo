t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    a.sort()
    is_j = True
    i = 0
    j = n - 1
    result = 0
    while j >= i:
        if is_j:
            result += a[j]
            j -= 1
        else:
            result -= a[i]
            i += 1

        is_j = not is_j

    print(result)
