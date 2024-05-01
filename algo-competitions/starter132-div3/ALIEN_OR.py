def answer(s, check):
    for e in s:
        if e not in check:
            return False
    return True


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(int(input(), 2))
    start = 1
    check_list = {start}
    for i in range(k - 1):
        start <<= 1
        check_list.add(start)

    print("YES" if answer(check_list, a) else "NO")
