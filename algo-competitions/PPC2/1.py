def answer(s: str):
    a_s, b, c_s = s
    a, c = int(a_s), int(c_s)
    if a == c:
        b = "="
    elif a > c:
        b = ">"
    else:
        b = "<"

    return f"{a}{b}{c}"


for _ in range(int(input())):
    print(answer(input()))
