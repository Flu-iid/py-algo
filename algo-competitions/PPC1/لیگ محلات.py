def plays(n: int):
    guide = list(range(n))
    result = []
    for first_i, e in enumerate(guide):
        for second_i in range(first_i + 1, n):
            result.append((first_i, second_i))
    return result


def read_score(n, scores):
    maps = dict()
    to_check = plays(n)
    for pair in to_check:
        team1, team2 = pair[0], pair[1]
        goal1 = scores[team1 * n + team2]
        goal2 = scores[team1 + team2 * n]
        # first score, second goal diff
        maps.setdefault(team1, [0, 0])
        maps.setdefault(team2, [0, 0])
        if goal1 == goal2:
            maps[team1][0] += 1
            maps[team2][0] += 1
        elif goal1 > goal2:
            maps[team1][0] += 3
            maps[team1][1] += goal1 - goal2

            maps[team2][1] += goal2 - goal1
        else:
            maps[team2][0] += 3
            maps[team2][1] += goal2 - goal1

            maps[team1][1] += goal1 - goal2

    return maps


def ranking(d: dict):
    return sorted(
        d.keys(), key=lambda k: d[k][0] * 10000 + d[k][1] * 100 - k, reverse=True
    )


n = int(input())
score_list = []
for i in range(n):
    score_list += [int(i) for i in input().split()]

maps = read_score(n, score_list)
ranks = ranking(maps)

for i in ranks:
    print(chr(ord("a") + i), end="")
