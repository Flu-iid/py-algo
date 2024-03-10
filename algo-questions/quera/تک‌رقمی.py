def num_summer(number: str):
    if len(number) == 1:
        return int(number)
    result = 0
    for c in number:
        result += int(c)
    return num_summer(str(result))


n = input()
print(num_summer(n))
