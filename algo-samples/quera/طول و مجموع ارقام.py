m, s = map(int, input().split(" "))


def max_maker(s, m):
    num_length = m
    digital_sum = s
    max_num = ""
    n = 0
    if s > m*9 or s < 1:
        return -1
    while digital_sum > 0:
        if digital_sum < 10:
            max_num += f"{digital_sum}"+(num_length-1)*"0"
            return int(max_num)
        else:
            max_num += "9"
            num_length -= 1
            digital_sum -= 9


def min_maker(s, m):
    if s > m*9 or s < 1:
        return -1
    max_num = max_maker(s, m)
    min_raw = str(max_num).strip("0")
    min_high, min_core = min_raw[-1], min_raw[:-1]
    min_core = min_core[::-1]
    min_zero = m-len(min_high)-len(min_core)
    return int(min_high+"0"*min_zero+min_core)


print(min_maker(s, m), max_maker(s, m))
