def answer(n):
    if n >= 100:
        return 0
    n_prime = 100 - n
    return n_prime - n_prime % 10


t = int(input())
for _ in range(t):
    x = int(input())
    print(answer(x))
