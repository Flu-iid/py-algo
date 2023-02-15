n = int(input())
string__input = input().split(" ")
p_list = [int(i) for i in string__input]

x_value = [100-i for i in p_list]

min_mamoor = 100 - sum(x_value)
if min_mamoor < 0:
    min_mamoor = 0

max_mamoor = min(p_list)

print(min_mamoor, max_mamoor)
