def correct_comparison(a: int, b: int):
    if a > b:
        return ">"
    elif a < b:
        return "<"
    else:
        return "="


def string_split(s: str):
    s_trans = s.translate(str.maketrans("<=>", "@@@"))
    a, b = map(int, s_trans.split("@"))
    return a, b


a, b = string_split(input())
comp = correct_comparison(a, b)
print(a, comp, b, sep="")
