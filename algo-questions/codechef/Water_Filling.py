for _ in range(int(input())):
    b = [int(i) for i in input().split()]
    answer = b.count(0)
    if answer > 1:
        print("Water filling time")
    else:
        print("Not now")
