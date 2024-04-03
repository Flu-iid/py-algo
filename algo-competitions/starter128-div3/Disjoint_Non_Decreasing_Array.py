t = int(input())


def solution(n: int, a: list):
    flag_consecutive = False
    increase_value = 0
    for i, e in enumerate(a):
        next = a[i + 1] if i < n - 1 else None
        if not next:  # handle end
            continue
        # pre = a[i-1] if i>0 else None
        if next < e:
            if flag_consecutive:
                return False

            tmp_increase = abs(e - next)
            a[i + 1] += tmp_increase
            flag_consecutive = True

            if not increase_value:
                increase_value = tmp_increase
            elif increase_value != tmp_increase:
                return False

        else:
            flag_consecutive = False
    return True


for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    print("Yes" if solution(n, a) else "No")


# def solution(n: int, a: list):
#     flag_consecutive = False
#     subsequence_distance = []
#     subsequence_index = []
#     for i, ele in enumerate(a):
#         pre = a[i - 1] if i > 0 else None
#         next = a[i + 1] if i < n - 1 else None
#         if not next:
#             s_length = len(subsequence_index)
#             if s_length == 1:
#                 one_ele = subsequence_distance[0]
#                 one_index = subsequence_index[0]
#                 if one_ele > (a[one_index] - a[one_index - 1]):
#                     return False
#             elif s_length == 0:
#                 return True
#             else:
#                 if len(set(subsequence_distance)) == 1:
#                     return True
#                 return False
#         elif (pre is None and ele <= next) or (pre and pre <= ele <= next):
#             flag_consecutive = False
#             continue
#         else:
#             if flag_consecutive:
#                 return False
#             subsequence_distance.append(ele - next)
#             subsequence_index.append(i)
#             flag_consecutive = True
