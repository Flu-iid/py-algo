from collections import deque
# graph = {
#     'f': ['g', 'i'],
#     'g': ['h'],
#     'h': [],
#     'i': ['g', 'k'],
#     'j': ['i'],
#     'k': []
# }


# def has_path(graph, src, dst):
#     stack = [src]
#     if src == dst:
#         return True
#     while stack:
#         c = stack.pop()
#         for n in graph[c]:
#             if n == dst:
#                 return True
#             stack.append(n)
#     return False


# print(has_path(graph, "f", "h"))


# edges = [
#     ('i', 'j'),
#     ('k', 'i'),
#     ('m', 'k'),
#     ('k', 'l'),
#     ('o', 'n')
# ]


# def to_graph(edges):
#     d = {}
#     for pair in edges:
#         d.setdefault(pair[0], set())
#         d.setdefault(pair[1], set())
#         d[pair[0]].add(pair[1])
#         d[pair[1]].add(pair[0])
#     return d


# def undirected_path(graph, src, dst):
#     if src == dst:
#         return True
#     memo = set()
#     q = deque([src])
#     while q:
#         c = q.pop()
#         memo.add(c)
#         for n in graph[c]:
#             if n == dst:
#                 return True
#             if n not in memo:
#                 q.appendleft(n)
#     return False


# print(to_graph(edges), undirected_path(to_graph(edges), "j", "m"))


# g = {
#     0: [8, 1, 5],
#     1: [0],
#     5: [0, 8],
#     8: [0, 5],
#     2: [3, 4],
#     3: [2, 4],
#     4: [3, 2]
# }


# def connected_components_count(graph):
#     memo = set(g.keys())
#     count = 0
#     while memo:
#         src = memo.pop()
#         stack = [src]
#         count += 1
#         while stack:
#             c = stack.pop()
#             if c in memo:
#                 memo.remove(c)
#             for n in graph[c]:
#                 if n in memo:
#                     stack.append(n)
#                     memo.remove(n)
#     return count


# print(connected_components_count(g))


# graph = {
#     0: [8, 1, 5],
#     1: [0],
#     5: [0, 8],
#     8: [0, 5],
#     2: [3, 4],
#     3: [2, 4],
#     4: [3, 2]
# }


# def largest_component(graph):
#     memo = set(graph.keys())
#     src = memo.pop()
#     max = src
#     q = deque([src])
#     while q:
#         c = q.popleft()
#         for n in graph[c]:
#             if n in memo:
#                 q.append(n)
#                 memo.remove(n)
#                 if n > max:
#                     max = n
#     return max


# print(largest_component(graph))


# graph = {
#     0: [8, 1, 5],
#     1: [0],
#     5: [0, 8],
#     8: [0, 5],
#     2: [3, 4],
#     3: [2, 4],
#     4: [3, 2]
# }


# def largest_component(graph):
#     all_key = set(graph.keys())
#     # sizes = []
#     size = 0
#     while all_key:
#         src = all_key.pop()
#         q = deque([src])
#         memo = set()
#         while q:
#             c = q.popleft()
#             memo.add(c)
#             for n in graph[c]:
#                 if n not in memo:
#                     q.append(n)
#                     memo.add(n)
#         # give all sizes
#         # sizes.append(len(memo))
#         tmp_size = len(memo)
#         size = tmp_size if tmp_size > size else size
#         all_key -= memo
#     return size


# print(largest_component(graph))


# edges = [
#     ['w', 'x'],
#     ['x', 'y'],
#     ['z', 'y'],
#     ['z', 'v'],
#     ['w', 'v']
# ]


# def shortest_path(edges, node_A, node_B):
#     if node_A == node_B:
#         return 0

#     def edge_to_graph(edges):
#         d = {}
#         for edge in edges:
#             d.setdefault(edge[0], set())
#             d.setdefault(edge[1], set())
#             d[edge[0]].add(edge[1])
#             d[edge[1]].add(edge[0])
#         return d
#     graph = edge_to_graph(edges)

#     memo = set()

#     q = deque([(node_A, 0)])
#     while q:
#         c, distance = q.popleft()
#         if c == node_B:
#             return distance
#         memo.add(c)
#         for n in graph[c[0]]:
#             if n == node_B:
#                 return distance+1
#             if n not in memo:
#                 q.append((n, distance+1))
#                 memo.add(n)
#     return -1


# print(shortest_path(edges, "w", "z"))


# grid = [
#     ['W', 'L', 'W', 'W', 'W'],
#     ['W', 'L', 'W', 'W', 'W'],
#     ['W', 'W', 'W', 'L', 'W'],
#     ['W', 'W', 'L', 'L', 'W'],
#     ['L', 'W', 'W', 'L', 'L'],
#     ['L', 'L', 'W', 'W', 'W'],
# ]


# def island_count(grid):
#     len_i, len_j = len(grid), len(grid[0])
#     land_memo = set()
#     count = 0

#     def bfs(i, j, val):
#         q = deque([(i, j)])
#         while q:
#             c = q.popleft()
#             land_memo.add(c)
#             x, y = c[0], c[1]
#             if x > 0 and grid[x-1][y] == val:
#                 new = (x-1, y)
#                 if new not in land_memo:
#                     q.append(new)
#                     land_memo.add(new)
#             if x < len_i-1 and grid[x+1][y] == val:
#                 new = (x+1, y)
#                 if new not in land_memo:
#                     q.append(new)
#                     land_memo.add(new)
#             if y > 0 and grid[x][y-1] == val:
#                 new = (x, y-1)
#                 if new not in land_memo:
#                     q.append(new)
#                     land_memo.add(new)
#             if y < len_j-1 and grid[x][y+1] == val:
#                 new = (x, y+1)
#                 if new not in land_memo:
#                     q.append(new)
#                     land_memo.add(new)

#     for i, g_i in enumerate(grid):
#         for j, g_j in enumerate(grid[i]):
#             if g_j == "L" and (i, j) not in land_memo:
#                 bfs(i, j, "L")
#                 count += 1

#     return count


# print(island_count(grid), island_count(grid=[
#     ['L', 'W', 'W', 'L', 'W'],
#     ['L', 'W', 'W', 'L', 'L'],
#     ['W', 'L', 'W', 'L', 'W'],
#     ['W', 'W', 'W', 'W', 'W'],
#     ['W', 'W', 'L', 'L', 'L'],
# ]),
#     island_count(grid=[
#         ['L', 'L', 'L'],
#         ['L', 'L', 'L'],
#         ['L', 'L', 'L'],
#     ]),
#     island_count(grid=[
#         ['W', 'W'],
#         ['W', 'W'],
#         ['W', 'W'],
#     ]))


# island 2

# grid = [
#     ['W', 'L', 'W', 'W', 'W'],
#     ['W', 'L', 'W', 'W', 'W'],
#     ['W', 'W', 'W', 'L', 'W'],
#     ['W', 'W', 'L', 'L', 'W'],
#     ['L', 'W', 'W', 'L', 'L'],
#     ['L', 'L', 'W', 'W', 'W'],
# ]


# def island_count(grid):
#     land_memo = set()
#     min_size = -1

#     def bfs(i, j, val):
#         tmp_land = set()
#         q = deque([(i, j)])
#         while q:
#             c = q.popleft()
#             tmp_land.add(c)
#             land_memo.add(c)
#             x, y = c
#             # inbounds
#             test = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
#             for i in test:
#                 if 0 <= i[0] < len(grid) and 0 <= i[1] < len(grid[i[0]]) and grid[i[0]][i[1]] == val and (i[0], i[1]) not in land_memo:
#                     new = (i[0], i[1])
#                     tmp_land.add(new)
#                     land_memo.add(new)
#                     q.append(new)
#         tmp_size = len(tmp_land)
#         if min_size == -1 or min_size > tmp_size:
#             return tmp_size
#         else:
#             return min_size

#     count = 0
#     for i, g_i in enumerate(grid):
#         for j, g_j in enumerate(grid[i]):
#             if (i, j) not in land_memo and g_j == "L":
#                 min_size = bfs(i, j, "L")
#                 count += 1
#     return count, min_size


# print(island_count(grid),
#       island_count(grid=[
#           ['L', 'L', 'L'],
#           ['L', 'L', 'L'],
#           ['L', 'L', 'L'],
#       ]),
#       island_count(grid=[
#           ['W', 'W'],
#           ['W', 'W'],
#           ['W', 'W'],
#       ]),
#       island_count(grid=[
#           ['L', 'W', 'W', 'L', 'W'],
#           ['L', 'W', 'W', 'L', 'L'],
#           ['W', 'L', 'W', 'L', 'W'],
#           ['W', 'W', 'W', 'W', 'W'],
#           ['W', 'W', 'L', 'L', 'L'],
#       ]),
#       island_count(grid=[
#           ['W', 'L', 'W', 'W', 'W'],
#           ['W', 'L', 'W', 'W', 'W'],
#           ['W', 'W', 'W', 'L', 'W'],
#           ['W', 'W', 'L', 'L', 'W'],
#           ['L', 'W', 'W', 'L', 'L'],
#           ['L', 'L', 'W', 'W', 'W'],
#       ]))
