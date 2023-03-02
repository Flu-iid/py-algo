m, s = [int(i) for i in input().split(" ")]
start, end = 10**(m-1), 10**(m)


def sum_dig(num):
    result = 0
    for i in str(num):
        result += int(i)
    return result


n = start
while n < end:
    print(n, sum_dig(n))
    n += 1
