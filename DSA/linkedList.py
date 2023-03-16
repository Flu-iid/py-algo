class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# ## 1st try
# def reverse_list(head,prev = None, tmp = None,index = 0):
#   if head==None:
#     prev.next = tmp
#     return prev
#   elif index==0:
#     index+=1
#     return reverse_list(head.next, head, None, index)
#   else:
#     prev.next = tmp
#     index += 1
#     return reverse_list(head.next, head, prev, index)


# ## 2nd try
# def reverse_list(head):
#     prev = None
#     tmp = None
#     while head != None:
#         tmp = prev
#         prev = head
#         head = head.next
#         prev.next = tmp
#     prev.next = tmp
#     return prev


# ## 3rd try
# def reverse_list(head):
#     prev = None
#     current = head
#     while current is not None:
#         next = current.next
#         current.next = prev
#         prev = current
#         current = next
#     return prev
