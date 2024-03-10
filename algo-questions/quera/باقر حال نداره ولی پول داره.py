# 10234
n, m = map(int, input().split())
kashi_ha = []
for i in range(n):
    kashi_ha.append(int(input()))

kashi_ha.sort(reverse=True)

cost = 0

before_m = sum([i**2 for i in kashi_ha])
