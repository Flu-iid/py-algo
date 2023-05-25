from collections import deque


class LLNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class TNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


a = LLNode("a")
b = LLNode("b")
c = LLNode("c")
a.next = b
b.next = c
# a -> b -> c

x = LLNode("x")
y = LLNode("y")
z = LLNode("z")
x.next = y
y.next = z
# x -> y -> z


def print_Llist(head):
    if head:
        print(head.val, end="|")
        return print_Llist(head.next)
    print()


def zipper_Llist(head1, head2, head1_prev=None, head2_prev=None, memo=list()):
    if head1 == None:
        head1_prev.next = head2_prev
    elif head2 == None:
        head1_prev.next = head2_prev
        head2_prev.next = head1
    else:
        if head1_prev:
            head1_prev.next = head2_prev
            head2_prev.next = head1
        return zipper_Llist(head1.next, head2.next, head1, head2, memo+[head1])
    return memo[0]


print_Llist(a)
print_Llist(x)
print_Llist(zipper_Llist(a, x))
