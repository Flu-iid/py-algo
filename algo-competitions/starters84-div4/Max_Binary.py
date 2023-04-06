for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    if s[0] == "0" and k > 0:
        s[0] = "1"
        k -= 1
    while k > 0:
        s.append("0")
        k -= 1
    print("".join(s))
