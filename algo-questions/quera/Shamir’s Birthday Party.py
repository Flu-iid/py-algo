for _ in range(int(input())):
    n, m = map(int, input().split())
    crush = set()
    for _ in range(m):
        u, v = map(int, input().split())
        crush.add(tuple(u, v))
