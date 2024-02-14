n, l = map(int, input().split())
# d = []  # distances
# r = []  # red lights
# g = []  # green lights
d = dict()

for i in range(n):
    k, v1, v2 = map(int, input().split())
    d[k] = {"r": v1, "g": v2}

result = 0
for step in range(1, l+1):
    result += 1
    if step in d:
        r, g = d[step]["r"], d[step]["g"]
        cycle_div, cycle_mod = divmod(result, r+g)
        # e.g. r is 2 when time passes 2 should be green so if cycle is green it should pass
        if cycle_mod < r:
            result += r - cycle_mod

print(result)
