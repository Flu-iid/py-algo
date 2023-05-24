from collections import deque

n = int(input())
edges = set()
for _ in range(n):
    pair = tuple([int(i) for i in input().split()])
    edges.add(pair)
print(edges)


def edge_to_graph(edges):
    graph = {}
    for edge in edges:
        graph.setdefault(edge[0], set())
        graph.setdefault(edge[1], set())
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


def bfs(graph, start, end):
    memo = set()
    if start not in graph:
        return False
    if start == end:
        return True
    q = deque([start])
    while q:
        c = q.popleft()
        if c == end:
            return True
        memo.add(c)
        for n in graph[c]:
            if n not in memo:
                q.append(n)
    return False


def dfs(graph, start, end):
    memo = set()
    path = set()
    tmp_path = []
    if start not in graph:
        return False
    if start == end:
        return True
    stack = [start]
    while stack:
        c = stack.pop()
        memo.add(c)
        tmp_path.append(c)
        if c == end:
            path.add(tuple(tmp_path))
            tmp_path.clear()
            memo.clear()
            memo.add(start)
        for n in graph[c]:
            if n not in memo:
                stack.append(n)
    return path


print(bfs(edge_to_graph(edges), start=1, end=5),
      dfs(edge_to_graph(edges), start=1, end=5))
