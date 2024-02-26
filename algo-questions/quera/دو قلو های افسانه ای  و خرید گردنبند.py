def circle_eq(s1: str, s2: str):
    s2 += s2
    reverse_s1 = "".join(reversed(s1))
    if s1 in s2 or reverse_s1 in s2:
        return True
    return False


for _ in range(int(input())):
    s1, s2 = input().split()
    print("YES" if len(s1) == len(s2) and circle_eq(s1, s2) else "NO")
