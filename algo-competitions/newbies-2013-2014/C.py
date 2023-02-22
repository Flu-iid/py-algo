t = int(input())
for i in range(t):
    n, r = [int(i) for i in input().split(" ")]
    planet_coordination = []
    for j in range(n):
        x, y = [int(i) for i in input().split(" ")]
        planet_coordination.append((x, y))

# need be >=180 degree
