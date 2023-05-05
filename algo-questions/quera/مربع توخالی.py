a = int(input())
b = int(input())
if b >= a:
    print("Wrong order!")
elif (a-b) % 2 != 0:
    print("Wrong difference!")
else:
    normal_row = int((a-b)/2)
    for _ in range(normal_row):
        print(a*"* ")
    for _ in range(b):
        print("* "*normal_row+"  "*b+"* "*normal_row)
    for _ in range(normal_row):
        print(a*"* ")
