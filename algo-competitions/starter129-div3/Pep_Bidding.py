for _ in range(int(input())):
    n = int(input())
    attA = sum([int(i) for i in input().split()])
    deffA = sum([int(i) for i in input().split()])
    attP = sum([int(i) for i in input().split()])
    deffP = sum([int(i) for i in input().split()])

    if attA > attP and deffA > deffP:
        print("A")
    elif attA < attP and deffA < deffP:
        print("P")
    else:
        print("DRAW")
