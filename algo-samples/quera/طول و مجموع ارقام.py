m, s = map(int, input().split(" "))


def max_maker(s, m):
    num_length = m
    digital_sum = s
    max_raw = ""
    n = 0
    if s > m*9 or s < 1:
        return -1
    while digital_sum > 0:
        if digital_sum < 10:
            max_raw += f"{digital_sum}"+(num_length-1)*"0"
            return int(max_raw)
        else:
            max_raw += "9"
            num_length -= 1
            digital_sum -= 9


def min_maker(s, m):
    if s > m*9 or s < 1:
        return -1
    max_raw = str(max_maker(s, m)).strip("0")
    if len(max_raw) == m:
        return max_raw[::-1]
    min_high, min_core = max_raw[-1], max_raw[:-1]
    min_zero = m-1-len(min_high)-len(min_core)
    return int("1"+"0"*min_zero+str(int(min_high)-1)+min_core)


print(min_maker(s, m), max_maker(s, m))
