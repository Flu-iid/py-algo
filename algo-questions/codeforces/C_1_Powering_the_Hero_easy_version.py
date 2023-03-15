t = int(input())

for i in range(t):
    n = int(input())
    s_deck = [int(i) for i in input().split(" ")]
    stack = []
    power = 0
    for item in s_deck:
        if item == 0:
            if stack:
                power += max(stack)
                del stack[stack.index(max(stack))]
        else:
            stack.append(item)
    print(power)
