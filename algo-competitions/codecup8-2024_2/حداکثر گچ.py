n = int(input())


def answer(n: int):
    mm = [i for i in range(2, n) if not n % i]
    if not mm:
        return [0, 1]  # [depth, child]
    result = [answer(m) for m in mm]
    result.sort(reverse=True, key=lambda x: x[0])
    max = result[0][0]
    child = 0
    for item in result:
        if item[0] == max:
            child += item[1]
    return [max+1, child]


result = answer(n)[1]
print(result % (10**9 + 7))
