graph = dict()
n, m = map(int, input().split())
for _ in range(m):
    u, v = map(int, input().split())
    graph.setdefault(v, set())
    graph.setdefault(u, set())
    graph[u].add(v)
    graph[v].add(u)
print(graph)

graph.pop()
# needs cycle counting. and consider it as need to changes
