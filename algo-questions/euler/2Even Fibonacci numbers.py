#!/bin/python3
memo = {1:1, 2:1}

def fibbo(n):
    if n not in memo:
        memo[n] = fibbo(n-2) + fibbo(n-1)
    return memo[n]

for _ in range(int(input())):
    number = int(input())
    n = 1
    result = []
    while number >= fibbo(n):
        if memo[n]%2==0:
            result.append(memo[n])
        n += 1
    print(sum(result))