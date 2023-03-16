from collections import deque


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f


# def depth_first_values(root):
#     if not root:
#         return []
#     stack = [root]
#     result = []
#     while stack:
#         c = stack.pop()
#         result.append(c.val)
#         if c.right:
#             stack.append(c.right)
#         if c.left:
#             stack.append(c.left)
#     return result


# print(depth_first_values(a))


# def breadth_first_values(root):
#     if not root:
#         return []
#     queue = deque([root])
#     result = []
#     while queue:
#         c = queue.pop()
#         result.append(c.val)
#         if c.left:
#             queue.appendleft(c.left)
#         if c.right:
#             queue.appendleft(c.right)
#     return result


# print(breadth_first_values(a))

# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f


# def tree_sum(root):
#     if not root:
#         return 0
#     stack = [root]
#     sum = 0
#     while stack:
#         c = stack.pop()
#         sum += c.val
#         if c.right:
#             stack.append(c.right)
#         if c.left:
#             stack.append(c.left)
#     return sum


# def tree_sum2(root):
#     if not root:
#         return 0
#     queue = deque([root])
#     sum = 0
#     while queue:
#         c = queue.pop()
#         sum += c.val
#         if c.right:
#             queue.appendleft(c.right)
#         if c.left:
#             queue.appendleft(c.left)
#     return sum


# print(tree_sum(a), tree_sum2(a))


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f


# def tree_includes(root, target):
#     if not root or not target:
#         return False
#     if root.val == target:
#         return True
#     q = deque([root])
#     while q:
#         c = q.pop()
#         if c.val == target:
#             return True
#         if c.right:
#             q.appendleft(c.right)
#         if c.left:
#             q.appendleft(c.left)
#     return False


# print(tree_includes(b, e))

# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f


# def tree_min_value(root):
#     stack = [root]
#     min = root.val
#     while stack:
#         c = stack.pop()
#         if c.val < min:
#             min = c.val
#         if c.right:
#             stack.append(c.right)
#         if c.left:
#             stack.append(c.left)
#     return min


# print(tree_min_value(a))


# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f


# def max_path_sum(root):
#     stack = [root]
#     max = None
#     while stack:
#         c = stack.pop()
#         if not c.right and not c.left:
#             if max:
#                 if max < c.val:
#                     max = c.val
#             else:
#                 max = c.val
#         if c[0].right:
#             stack.append([c[0].right, c[1] + c[0].right.val])
#         if c[0].left:
#             stack.append([c[0].left, c[1] + c[0].left.val])
#     return max


# print(max_path_sum(a))
