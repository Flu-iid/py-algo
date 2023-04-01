n = int(input())

a = [int(i) for i in input().split()]

payan = max(a)
all = sum(a)

print(all-2*payan, payan)
