a, b = int(input()), int(input())

if b >= a:
    print("Wrong order!")

elif (a - b) % 2:
    print("Wrong difference!")

else:
    edge = (a - b) // 2
    for row in range(a):
        print("* " * edge, end="")
        print("* " * b, end="") if row < edge or row >= edge + b else print(
            "  " * b, end=""
        )
        print("* " * edge)
