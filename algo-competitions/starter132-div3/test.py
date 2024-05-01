start = 1
check_list = [start]
for i in range(3):
    start <<= 1
    check_list.append(start)

print(check_list)
