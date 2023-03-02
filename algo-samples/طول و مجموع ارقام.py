m, s = [int(i) for i in input().split(" ")]
start, end = 10**(m-1), 10**(m)


def sum_dig(num):
    result = 0
    for i in str(num):
        result += int(i)
    return result


n = start
min, max = -1, -1
while n < end:
    if sum_dig(n) == s:
        if min == -1 and max == -1:
            min, max = n, n
        else:
            max = n
    n += 1

print(min, max)
