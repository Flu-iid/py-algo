def answer(n, m, l_n: list, l_m: list):
    if (n + m) < 11 or n < 4 or m < 4:
        return 0
    l_n.sort()
    l_m.sort()
    team = []
    for _ in range(4):
        team.append(l_m.pop())
        team.append(l_n.pop())
    left_over = l_m + l_n
    left_over.sort()
    return sum(team) + sum(left_over[-3:])


t = int(input())
for _ in range(t):
    bat, bowl = map(int, input().split())
    bat_skill = [int(i) for i in input().split()]
    bowl_skill = [int(i) for i in input().split()]
    result = answer(bat, bowl, bat_skill, bowl_skill)
    print(result if result else -1)
