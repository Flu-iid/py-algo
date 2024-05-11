t = int(input())
for _ in range(t):
    legs = int(input())
    count = 0
    while legs >= 4:
        count += 1
        legs -= 4
    else:
        count += legs // 2
    print(count)
