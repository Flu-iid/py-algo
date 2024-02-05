class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def reverse(node, prev_node=None):
    if node == None:
        return prev_node
    tmp = node.next
    node.next = prev_node
    return reverse(tmp, node)


def traverse(node, r=list()):
    if node == None:
        return r
    r += [node.val]
    return traverse(node.next, r)


def zipper(head1, head2, prev_head1=None, prev_head2=None, head=None):
    if not head:
        head = head1
    if not head1:
        prev_head1.next = prev_head2
        return head
    if not head2:
        prev_head1.next = prev_head2
        prev_head2.next = head1
        return head
    if prev_head1 and prev_head2:
        prev_head1.next = prev_head2
        prev_head2.next = head1
    return zipper(head1.next, head2.next, head1, head2, head)


a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z

# print(traverse(zipper(a, x)))


def acroman(a, b):
    if a == 0:
        return b+1
    elif b == 0:
        return acroman(a-1, 1)
    return acroman(a-1, acroman(a, b-1))


print(acroman(2, 2))
