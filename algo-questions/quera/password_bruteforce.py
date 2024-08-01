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


def counter(s: str) -> int:
    l = len(s)
    output = 0
    if l == 1 or l == 2:
        output += 9
    elif l == 3:
        if s[0] == [2]:
            output += 3
        else:
            output += 15
    elif l == 4:
        if s[0] != s[2]:
            output += 4
        if s[1] != s[3]:
            output += 5
        else:
            output += 1
    elif l == 5:
        if s[0] == s[2] == s[4]:
            pass
        elif s[0] == s[2] != s[4]:
            output += 2
        elif s[0] != s[2] == s[4]:
            output += 2
        elif s[0] != s[2] != s[4]:
            if s[1] != s[3]:
                output += 4
            else:
                output += 8
    elif l == 6:
        if s[0] == s[2] != s[4]:
            if s[1] == s[3] != s[5]:
                output += 1
        elif s[0] != s[2] != s[4]:
            if s[1] == s[3] != s[5]:
                output += 2
        elif s[0] != s[2] == s[4]:
            if s[1] == s[3] != s[5]:
                output += 3
            elif s[1] == s[3] == s[5]:
                output += 1
            elif s[1] != s[3] != s[5]:
                output += 2
    return output


if __name__ == "__main__":
    a = input()
    if check_rule(a):
        print(counter(a))
    else:
        print(0)
