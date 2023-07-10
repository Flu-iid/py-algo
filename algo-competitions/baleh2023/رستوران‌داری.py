n = int(input())
d = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
table_dict = {}
for i in range(n):
    table_dict.setdefault(d[i], t[i])
base = min(table_dict.keys())
price = table_dict[base]
del table_dict[base]
while table_dict:
    current = min(table_dict.keys())
    current_price = table_dict[current]
    if current_price <= abs(current-base):  # stick_new
        price += current_price
        base = current
    else:
        price += abs(current-base)
    del table_dict[current]
print(price)
