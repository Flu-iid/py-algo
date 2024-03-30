#!/bin/python3

def msum(n, multi):
    max = (n-1)//multi
    return (max*(max+1)//2)*multi

for _ in range(int(input())):
    n = int(input())
    print(msum(n, 3)+msum(n, 5)-msum(n, 15))