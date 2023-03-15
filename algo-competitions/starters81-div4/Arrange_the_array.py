t = int(input())
for i in range(t):
    n = int(input())
    array = [int(i) for i in input().split()]
    s = sorted(array)
    min_div = 0
    index = [0, 0]
    for i in range(n):
        if i == 0:
            pass
        if s[i] == s[i-1]:
            pass
        else:
            if min_div == 0:
                min_div = abs(s[i]-s[i-1])
                index = [i-1, i]
            elif min_div > abs(s[i]-s[i-1]):
                min_div = abs(s[i]-s[i-1])
                index = [i-1, i]
    s[index[0]], s[index[1]] = s[index[1]], s[index[0]]
    print(" ".join(map(str, s)))
