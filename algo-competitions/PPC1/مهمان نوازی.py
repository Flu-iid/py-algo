n, d = map(int, input().split())
sleep_place = [int(i) for i in input().split()]

sleep_place.sort()

index = min(sleep_place)

covered = 0
count = 0
for e in sleep_place:
    if covered < e:
        covered = e + d
        count += 1

print(count)
