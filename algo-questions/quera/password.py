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


#
#
# def counter(s: str) -> int:
#     l = len()
#     if l == 1 or l == 2:
#         return 9
#     elif l == 3:
#         if s[0] == [2]:
#             return 3
#         else:
#             return 15
#     elif l == 4:
#         if s[0] != s[2]:
#             return 3
#         elif s[1] != s[3]:
#             return 4
#         else:
#             return 1
#     elif l == 5:
#         if s[0] == s[-1] and s[1] == s[-2]:
#             return 5
#         elif s[0] == s[2] and s[1] == s[3]:
#             return 2
#         else:
#             return 1
#     elif l == 6:
#         pass


# 2 solvable ways
# 1 brute force: with contradictions
# 2 using graph theory


graph: dict = {
    1: {"R": [2, 3], "D": [4, 7], "L": [], "U": []},
    2: {"R": [3], "D": [5, 8], "L": [1], "U": []},
    3: {"R": [], "D": [6, 9], "L": [1, 2], "U": []},
    4: {"R": [5, 6], "D": [7], "L": [], "U": [1]},
    5: {"R": [6], "D": [8], "L": [4], "U": [2]},
    6: {"R": [], "D": [9], "L": [4, 5], "U": [3]},
    7: {"R": [8, 9], "D": [], "L": [], "U": [1, 4]},
    8: {"R": [9], "D": [], "L": [7], "U": [2, 5]},
    9: {"R": [], "D": [], "L": [7, 8], "U": [3, 6]},
}


def count_one_to_all(start: int, path: str, visited: list = []) -> int:
    if not path:
        visited = []
        return 1
    c = path[0]
    if not graph[start][c]:
        visited = []
        return 0
    count = []
    for next_node in graph[start][c]:
        if next_node not in visited:
            count.append(count_one_to_all(next_node, path[1:], visited+[start]))
    return sum(count)


def count_all_to_all(s: str):
    return sum([count_one_to_all(k, s) for k in graph])
    # for k in graph:
    #     print(k, count_one_to_all(k, s))


if __name__ == "__main__":
    a = "RDL"
    if check_rule(a):
        print(count_all_to_all(a))
    else:
        print(0)