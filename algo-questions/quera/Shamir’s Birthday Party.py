def check(graph):
    count = 0
    for n in graph:
        if not graph[n]:
            return 1


for _ in range(int(input())):
    n, m = map(int, input().split())
    crush = set()
    for _ in range(m):
        u, v = map(int, input().split())
        crush.add((u, v))
    graph = {}
    for edge in crush:
        p1, p2 = edge
        graph.setdefault(p1, set())
        graph.setdefault(p2, set())
        graph[p1].add(p2)
