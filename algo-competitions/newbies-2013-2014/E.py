contents = []
count = 1
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
# clean content
lines = []

while contents:
    l_num = int(contents[0])
    lines.append(contents[1:l_num+1])
    contents = contents[l_num+1:]
print(lines)

count = 1
for case in lines:
    d = {}
    for i in case:
        string_input = i.split(" ")
        myman, pool, n = string_input[0].lower(), int(
            string_input[1]), int(string_input[2])
        debtor_list = [i.lower() for i in string_input[3:]]
        for man in debtor_list:
            if man not in d:
                d[man] = 0
        debtor_list.remove(myman)
        myman_credit = int(pool * (n-1)/n)
        debt = int(pool/n)
        #
        d[myman] += myman_credit
        for man in debtor_list:
            d[man] -= debt
    debtors, creditors = [], []
    for key, value in d.items():
        if value > 0:
            creditors.append((key.title(), value))
        elif value < 0:
            debtors.append((key.title(), abs(value)))
    print(f"Case #{count}:")
    count += 1
    print("Debtors:")
    debtors.sort()
    creditors.sort()
    for i in debtors:
        print(i[0], "owes", i[1], "Tomans.")
    print("Creditors:")
    for i in creditors:
        print(i[0], "paid", i[1], "Tomans.")
