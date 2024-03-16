n, l = map(int, input().split())
events = []
for _ in range(n):
    events.append(tuple([int(i) for i in input().split()]))

events.sort(reverse=True, key=lambda x: x[1]-x[0])

print(events)

# sweep line
