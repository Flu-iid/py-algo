n, m, k = [int(i) for i in input().split(" ")]
d = {}
flag = 1 <= n <= 1000 and 1 <= m <= 1000 and 0 <= k <= 1000
# 1 healthy , 0 jammed
for i in range(1, n+1):
    for j in range(1, m+1):
        d[(i, j)] = 1

for key in range(k):
    k_i, k_j = [int(i) for i in input().split(" ")]
    if (k_i, k_j) in d:
        d[(k_i, k_j)] = 0

if __name__ == "__main__" and flag:
    if n*m-k == 0:
        print(-1)
    elif k % 2:
        print(0)
    else:
        k += 1
        if n*m-k == 0:
            print(-1)
        else:
            print(1)
            for key in sorted(d):
                if d[key] == 1:
                    print(*key)
                    break
