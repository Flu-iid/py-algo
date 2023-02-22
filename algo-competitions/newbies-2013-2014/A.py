t = int(input())
for i in range(t):
    n, t1, t2 = [int(i) for i in input().split(" ")]
    print(t1*n + (n-1)*t2)
