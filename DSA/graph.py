# edges = [{"i", "j"},
#          {"k", "i"},
#          {"m", "k"},
#          {"k", "l"},
#          {"o", "n"}]

# adjacency list
# graph = {}
# for edge in edges:
#     p1, p2 = edge
#     graph.setdefault(p1, set())
#     graph.setdefault(p2, set())
#     graph[p1].add(p2)
#     graph[p2].add(p1)
# print(graph)

# memo = set()

# def dft(graph, src, dst):
#     memo.add(src)
#     if src == dst:
#         return True
#     for neighbor in graph[src]:
#         if neighbor not in memo:
#             if dft(graph, neighbor, dst):
#                 return True
#     return False


# print(dft(graph, "i", "l"))


# def make_undirected_graph(edges):
#     graph = {}
#     for edge in edges:
#         p1, p2 = edge
#         graph.setdefault(p1, set())
#         graph.setdefault(p2, set())
#         graph[p1].add(p2)
#         graph[p2].add(p1)
#     return graph


# def dft(graph, src, dst, memo=set()):
#     memo.add(src)
#     if src == dst:
#         return True
#     for neighbor in graph[src]:
#         if neighbor not in memo:
#             if dft(graph, neighbor, dst, memo):
#                 return True
#     return False


# graph = {3: set(),
#          4: {6},
#          6: {4, 5, 7, 8},
#          8: {6},
#          7: {6},
#          5: {6},
#          1: {2},
#          2: {1}}

# print(dft(graph, 4, 5))
