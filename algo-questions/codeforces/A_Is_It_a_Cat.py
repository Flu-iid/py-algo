# t = int(input())


# def check(s, n):
#     check_list = list("meow")
#     result = []
#     if s[0] != "m" or s[-1] != "w":
#         return False
#     else:
#         for i in range(n):
#             if i == 0:
#                 result.append(s[i])
#             elif s[i] != result[-1]:
#                 result.append(s[i])
#     return result == check_list


# for i in range(t):
#     n = int(input())
#     s = input().lower()
#     print("YES") if check(s, n) else print("NO")


# 2
def accept(s: str, n: int):
    guide = "meow"
    check = ""
    for i in range(n):
        check += s[i].lower() if i == 0 or s[i -
                                             1].lower() != s[i].lower() else ""
    return check == guide


for _ in range(int(input())):
    n = int(input())
    s = input()
    print("YES" if accept(s, n) else "NO")
