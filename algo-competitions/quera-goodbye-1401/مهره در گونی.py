n, m = map(int, input().split())
d = {}
for _ in range(m):
    l, r, x = map(int, input().split())
    for i in range(l, r+1):
        d.setdefault(i, set())
        d[i].add(x)

for i in range(1, n+1):
    d.setdefault(i, [])
    if d[i]:
        if min(d[i]) > 1:
            print(1, end=" ")
        else:
            stake = set(range(1, max(d[i])+1)) - set(d[i])
            if stake:
                print(min(stake), end=" ")
            else:
                print(max(d[i])+1, end=" ")
    else:
        print(1, end=" ")
