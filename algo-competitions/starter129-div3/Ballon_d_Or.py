t = int(input())
for _ in range(t):
    n = int(input())
    count_2 = sum([1 if i == "2" else 0 for i in input().split()])
    if count_2 % 8 == 0:
        print("YES")
    else:
        print("NO")
