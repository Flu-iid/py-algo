n, m = map(int, input().split())
g = {}
sum = 0
lowest = 0
start = 0
for _ in range(m):
    i, j, w = map(int, input().split())
    g.setdefault(i, {})
    g.setdefault(j, {})
    g[i][j] = w
    g[j][i] = w
    start = i if lowest == 0 or w < lowest else start


def dfs(start_node: int, graph: dict, sum: int = 0, result: int = 0):
    memo = set()
    s = [start_node]
    while s:
        c = s.pop()
        memo.add(c)
        if c in memo:
            result = sum if sum < result or result == 0 else result
        for n, v in graph[c].items():
            if n not in memo:
                s.append(n)
                sum += v
    return result


print(dfs(start, g))

# wrong traverse
