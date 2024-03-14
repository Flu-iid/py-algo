n, amin_v = map(int, input().split())
juice_map = dict()
for _ in range(n):
    tmp_h, tmp_v = map(int, input().split())
    true_happiness = tmp_h / tmp_v
    juice_map[true_happiness] = juice_map.get(true_happiness, 0) + tmp_v


happiness = 0
for h in sorted(juice_map.keys(), reverse=True):  # h -> true happiness
    if amin_v == 0:
        break
    else:
        v = juice_map[h]
        if amin_v >= v:
            happiness += h*v
            amin_v -= v
        else:
            happiness += h * amin_v
            amin_v = 0


print(round(happiness, 1))
