t = int(input())
for i in range(t):
    d = {}
    n, m = [int(i) for i in input().split(" ")]
    prize_list = [int(i) for i in input().split(" ")]
    for j in range(m):
        u, v, w = [int(i) for i in input().split(" ")]
        d[{u, v}] = w
    keys = d.keys()
    for index in range(1, len(prize_list)+1):
        if index in keys:
