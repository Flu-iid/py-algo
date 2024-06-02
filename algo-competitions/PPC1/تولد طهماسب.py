n = int(input())

degrees = [float(i) for i in input().split()]
degrees.sort()

degree_prime = []
for i in range(n - 1):
    degree_prime.append(degrees[i + 1] - degrees[i])

degree_prime.append(360 - sum(degree_prime))

print(max(degree_prime) * 100 / 360)
