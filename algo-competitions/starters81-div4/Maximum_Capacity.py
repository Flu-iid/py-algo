t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    if x <= 8 and x*y <= 500:
        print("YES")
    else:
        print("NO")
