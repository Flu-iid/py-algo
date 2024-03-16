
# bot cant have R
# top cant have L
# no two R or L


def snake(s: str):
    top = ["0" for i in range(8)]
    bot = ["0" for i in range(8)]
    bot[0] = "1"

    if "LL" in s or "RR" in s:
        return "DEATH"
    state = False  # state False means bot | True means top
    for i in range(0, 7):
        if (s[i] == "L" and state == True) or (s[i] == "R" and state == False):
            return "DEATH"
        if s[i] == "F":
            if state:
                top[i+1] = "1"
            else:
                bot[i+1] = "1"
        elif s[i] == "R":
            state = False
            bot[i+1] = "1"
        elif s[i] == "L":
            state = True
            top[i+1] = "1"
    return "".join(top) + "\n" + "".join(bot)


print(snake(input()))
