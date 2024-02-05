for _ in range(int(input())):
    n, k = map(int, input().split())
    share = int(n/(k+1))
    print(n - share*k)
