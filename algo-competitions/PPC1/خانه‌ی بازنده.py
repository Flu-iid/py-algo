def looser_row(a, n, i, j):
    target = a[i][j]
    if n == 1:
        return True
    if j == 0:
        if target > a[i][j + 1]:
            return False
    if j == n - 1:
        if target > a[i][j - 1]:
            return False
    else:
        if target > a[i][j - 1] or target > a[i][j + 1]:
            return False
    return True


def looser_col(a, n, i, j):
    target = a[i][j]
    if n == 1:
        return True
    if i == 0:
        if target > a[i + 1][j]:
            return False
    if i == n - 1:
        if target > a[i - 1][j]:
            return False
    else:
        if target > a[i - 1][j] or target > a[i + 1][j]:
            return False
    return True


n = int(input())
a = []
for _ in range(n):
    a.append([int(i) for i in input().split()])

count = 0
for i in range(n):
    for j in range(n):
        if looser_col(a, n, i, j) and looser_row(a, n, i, j):
            count += 1

print(count)


# def check(a, n, i_e):
#     i, j = i_e // n, i_e % n
#     goal = a[i * n + j]
#     flag = True
#     i_neighbours, j_neighbours = [], []
#     if 0 < i < n - 1:
#         i_neighbours += [i - 1, i + 1]
#     elif i == 0:
#         i_neighbours += [i + 1]
#     else:
#         i_neighbours += [i - 1]
#     if 0 < j < n - 1:
#         j_neighbours += [j - 1, j + 1]
#     elif j == 0:
#         j_neighbours += [j + 1]
#     else:
#         j_neighbours += [j - 1]

#     for row in i_neighbours:
#         if a[row * n + j] < goal:
#             flag = False
#     for col in j_neighbours:
#         if a[i * n + col] < goal:
#             flag = False
#     return flag


# n = int(input())
# a = []
# for _ in range(n):
#     a += [int(i) for i in input().split()]

# count = 0
# for square_index in range(n):
#     if check(a, n, square_index):
#         count += 1

# print(count)
