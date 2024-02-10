# # x = input()

# def x_map(x: str) -> list:
#     """
#     to sort what numbers does x have inorder
#     """
#     l = []
#     for i in x:
#         if i not in l:
#             l.append(i)
#     l.sort()
#     return l


# def min_max(x):
#     if len(x) < 2:
#         return x
#     elif len(x) == 2:
#         if x[-1] <= x[0]:
#             return x
#         else:
#             return x[-1]+x[0]
#     else:
#         pass

# the solution is to solve it recurrsively. given thatif u cant fix the number in smaller recursions
# we would take the bigger one . put bigger number infront and sort the rest accordingley


# but simpler solution will be to generate every number and save the number we want with the
# given condiditon

x = input()


def str_to_dict(s: str) -> dict:
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def number_generator(m: dict) -> list:
    l = list()
    for i in m:
        tmp_m = m.copy()
        tmp_m[i] -= 1
        if tmp_m[i] == 0:
            del tmp_m[i]
        if not tmp_m:
            l.append(i)
        else:
            for j in number_generator(tmp_m):
                l.append(i+j)

    return l


low = 0
for n in number_generator(str_to_dict(x)):
    if x < n and (low == 0 or low > n):
        low = n

print(low)
