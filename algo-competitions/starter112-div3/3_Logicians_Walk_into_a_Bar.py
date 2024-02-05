for _ in range(int(input())):
    n = int(input())
    s = input()
    no_flag = False
    for c in range(n):
        if s[c] == "0":
            no_flag = True
            print("NO")
        elif no_flag:
            print("NO")
        elif c == n-1 and not no_flag:
            print("YES")
        else:
            print("IDK")
