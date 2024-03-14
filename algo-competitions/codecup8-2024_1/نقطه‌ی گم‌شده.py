# problem if it wasnt paralel to x,y,z axises
# cube = list()
# for i in range(7):
#     x, y, z = map(int, input().split())
#     cube.append((x, y, z))


# def dist2(cord1: tuple, cord2: tuple):
#     return (cord1[0] - cord2[0])**2 + (cord1[1] - cord2[1])**2+(cord1[2] - cord2[2])**2


# question_cord = None
# center_cord = None
# for cord1 in cube:
#     cord_distances = []
#     for cord2 in cube:
#         cord_distances.append((dist2(cord1, cord2), cord1, cord2))
#     cord_distances.sort(reverse=True)
#     if cord_distances[0][0] == cord_distances[1][0]:
#         question_cord = cord1
#     else:
#         dist, (x1, y1, z1), (x2, y2, z2) = cord_distances[0]
#         center_cord = (x1+x2, y1+y2, z1+z2)

# for i in range(3):
#     print(center_cord[i]-question_cord[i], end=" ")


# with xor
x = 0
y = 0
z = 0
for i in range(7):
    a1, a2, a3 = [int(i) for i in input().split()]
    x ^= a1
    y ^= a2
    z ^= a3
print(x, y, z)
