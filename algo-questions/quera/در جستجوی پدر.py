def check_prime(a):
    if a < 2:
        return False
    if a == 2:
        return True
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def prime_sum(a):
    if a < 2:
        return 0
    elif a == 2:
        return 2
    sum = 0
    for i in range(2, int(a/2)):
        if check_prime(i) and not a % i:
            sum += i
    return sum


def number_sum(a):
    l = list(str(a))
    sum = 0
    for i in l:
        sum += int(i)
    return sum


def d(a):
    return a+number_sum(a)+prime_sum(a)


for _ in range(int(input())):
    n = int(input())
    flag = False
    for i in range(4, n):
        if d(i) == n:
            print("Yes")
            flag = True
            break
    if flag == False:
        print("No")
