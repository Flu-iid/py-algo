import sys
import io
import os
import collections
import heapq

edges = {("a", "c"),
         ("a", "b"),
         ("c", "e"),
         ("e", "b"),
         ("b", "d"),
         ("f", "d")}

graph = {}
for i in edges:
    p1, p2 = i
    graph.setdefault(p1, set())
    graph.setdefault(p2, set())
    graph[p1].add(p2)


def dft(graph, src):
    stack = [src]
    while len(stack) > 0:
        tmp = stack.pop()
        print(tmp)
        for n in graph[tmp]:
            stack.append(n)


dft(graph, "a")


def bft(graph, src):
    dq = collections.deque
    queue = dq(src)
    while len(queue) > 0:
        tmp = queue.pop()
        print(tmp)
        for n in graph[tmp]:
            queue.appendleft(n)


print("-")
bft(graph, "a")

# def fast_io():

#     # Reinitialize the Input function
#     # to take input from the Byte Like
#     # objects
#     input = io.BytesIO(os.read(0,
#                                os.fstat(0).st_size)).read

#     # Taking input as string
#     return input().decode()


# sys.stdout.write(fast_io())


# print([1, 1, 1, 2, 3].count(1))
# heapq.heapify([1])
# print(collections.deque([1, 2, 3, 4, 5]))
# print([1, "hello", True])
