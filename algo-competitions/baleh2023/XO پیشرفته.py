n, a = map(int, input().split())
a = {}
for i in range(n):
    s = input()
    for j in range(len(s)):
        a[(i, j)] = s[j]

# row move
for i in range(n):
    for j in range(n):
        pass
