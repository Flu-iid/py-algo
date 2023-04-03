from collections import deque as dq
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    edges = set()
    for _ in range(m):
        pair = tuple([int(i) for i in input().split()])
        edges.add(pair)
    # make graph
    graph = {}
    for edge in edges:
        p1, p2 = edge
        graph.setdefault(p1, set())
        graph.setdefault(p2, set())
        graph[p1].add(p2)
        graph[p2].add(p1)
    # 2 step from 1
    src = [1, 0]
    memo = set([src[0]])
    result = set()
    q = dq([src])
    while q:
        c_val, c_step = q.popleft()
        if c_step == 2:
            result.add(c_val)
        for n in graph[c_val]:
            if n not in memo:
                memo.add(n)
                q.append([n, c_step+1])

    print(len(result))
