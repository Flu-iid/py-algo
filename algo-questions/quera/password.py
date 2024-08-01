direction = ["R", "D", "U", "L"]
contradiction = [{"L", "R"}, {"U", "D"}]


def check_rule(s: str) -> bool:
    for i, c in enumerate(s):
        if c not in direction:
            return False
        if i != 0 and c == s[i - 1]:
            return False
        if i != 0 and {c, s[i - 1]} in contradiction:
            return False
    return True


graph: dict = {
    1: {"R": [2, 3], "D": [4, 7], "L": [], "U": []},
    2: {"R": [3], "D": [5, 8], "L": [1], "U": []},
    3: {"R": [], "D": [6, 9], "L": [2, 1], "U": []},
    4: {"R": [5, 6], "D": [7], "L": [], "U": [1]},
    5: {"R": [6], "D": [8], "L": [4], "U": [2]},
    6: {"R": [], "D": [9], "L": [5, 4], "U": [3]},
    7: {"R": [8, 9], "D": [], "L": [], "U": [4, 1]},
    8: {"R": [9], "D": [], "L": [7], "U": [5, 2]},
    9: {"R": [], "D": [], "L": [8, 7], "U": [6, 3]},
}


def count_one_to_all(start: int, path: str, visited: list = []) -> int:
    if not path:
        return 1
    c = path[0]
    if not graph[start][c]:
        return 0
    count = []
    for i, next_node in enumerate(graph[start][c]):
        if next_node not in visited:
            if i == 1 and graph[start][c][0] not in visited:
                count.append(
                    count_one_to_all(
                        next_node, path[1:], visited + [start, graph[start][c][0]]
                    )
                )
            elif i == 0:
                count.append(count_one_to_all(next_node, path[1:], visited + [start]))
    return sum(count)


def count_all_to_all(s: str):
    # for k in graph:
    #     print(k, count_one_to_all(k, s))
    return sum([count_one_to_all(k, s) for k in graph])


if __name__ == "__main__":
    a = input()
    if check_rule(a):
        # print(count_one_to_all(4, a))
        print(count_all_to_all(a))
    else:
        print(0)
