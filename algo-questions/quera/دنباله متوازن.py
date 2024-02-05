# d = {"(": 1, ")": -1}
s = input()
sum = 0
change = 0
while s:
    c = s[0]
    if c == ")":
        if sum <= 0:
            change += 1
            sum += 1
        else:
            sum -= 1
    elif c == "(":
        if len(s) == 1:
            change += 1
            sum -= 1
        else:
            sum += 1
    s = s[1:]
print(sum//2 + change)
