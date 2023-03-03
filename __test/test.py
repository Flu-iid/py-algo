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
            return max_num
        else:
            max_num += "9"
            num_length -= 1
            digital_sum -= 9


print(max_maker(0, 2))
