# import random
# import math


# a = [10, 3, 1, 7, 3, 6, 9]
# b = []
# m = math.factorial(len(a))
# while len(b) < m:
#     random.shuffle(a)
#     if a not in b:
#         b += [a]
# print(b)

# def min_surf_fn(d_list):
#     minmum_surface = 0
#     for di in range(len(d_list)):
#         if di+1 == len(d_list):
#             minmum_surface += (d_list[di]**2)*5
#         else:
#             minmum_surface += (d_list[di]**2)*4 + \
#                 abs(d_list[di]**2 - d_list[di+1]**2)
#     print(minmum_surface)


# line_list = input().split(" ")
# madar_kharj, kharj, tedad_bacheha,  \
#     bacheha = line_list[0], line_list[1], line_list[2], line_list[3:]

# print(madar_kharj, kharj, tedad_bacheha, bacheha)
a = [1, 2, 3, 4]
a[1:3] = [2, 2]
print(a)
