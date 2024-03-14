from itertools import chain, combinations
from math import ceil, floor


def mashq(a: list):
    n = len(a)
    if n == 0:
        return 0
    upper = int(n/2)
    lower = int(n/2) + 1 if n % 2 else int(n/2)
    sum_upper = sum(a[lower:])
    sum_lower = sum(a[:lower])
    return sum_upper - sum_lower


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


n = int(input())
a = [int(i) for i in input().split()]

answer = 0
for i in powerset(a):
    # print(i, mashq(i))
    answer += mashq(i)
print(answer % (10**9 + 7))
