# 1
# int_a, int_b = int(input().replace(" ", ""), 2), int(
#     input().replace(" ", ""), 2)
# print(bin(int_a & int_b).count("1"))


# 2
a, b = input().split(), input().split()
count = 0
for i in range(8):
    if a[i] == b[i] == "1":
        count += 1
print(count)
