for _ in range(int(input())):
    a = [int(i) for i in input().split()]
    ans = a.index(min(a))
    if ans == 0:
        print("ALICE")
    elif ans == 1:
        print("BOB")
    elif ans == 2:
        print("CHARLIE")
