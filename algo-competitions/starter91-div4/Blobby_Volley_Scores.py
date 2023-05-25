for _ in range(int(input())):
    n = int(input())
    s = input().lower()
    turn = "a"
    score = {"a": 0, "b": 0}
    for c in s:
        if c == turn:
            score[c] += 1
        else:
            turn = c
    print(score["a"], score["b"])
