a, b, c = int(input()), int(input()), int(input())
l = sorted([a, b, c])
if l[2]**2 == l[0]**2+l[1]**2:
    print("YES")
else:
    print("NO")
