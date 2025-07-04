def check(n: str):
    if n[:2] == "09" and len(n) == 11 and n.isdigit():
        return "+98" + n[1:]
    elif n[:2] == "98" and len(n) == 12 and n.isdigit():
        return "+" + n
    elif n[:3] == "+98" and len(n) == 13 and n[1:].isdigit():
        return n
    else:
        return "invalid"

for _ in range(int(input())):
    number = input()
    print(check(number))