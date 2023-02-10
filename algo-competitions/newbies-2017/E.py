t = int(input())
for i in range(t):
    l = int(input())
    dorm_dict = {}
    for line in range(l):
        line_list = input().split(" ")
        madar_kharj, kharj, tedad_bacheha, bacheha = line_list[0].lower().title(), int(
            line_list[1]), int(line_list[2]), line_list[3:]
        bacheha = [item.lower().title() for item in bacheha]
        # minus for creditor and plus for debtor
        if madar_kharj not in dorm_dict.keys():
            dorm_dict[madar_kharj] = 0
        dorm_dict[madar_kharj] -= kharj
        for b in bacheha:
            if b not in dorm_dict.keys():
                dorm_dict[b] = 0
            dorm_dict[b] += int(kharj/tedad_bacheha)
    # get lists
    debtor_name = []
    creditor_name = []
    debtor_value = []
    creditor_value = []
    for k in dorm_dict:
        if dorm_dict[k] > 0:
            debtor_name.append(k)
        elif dorm_dict[k] < 0:
            creditor_name.append(k)
    debtor_name.sort()
    creditor_name.sort()

    # print results
    print(f"Case #{i+1}:")
    print("Debtors:")
    for name in debtor_name:
        print(name, "owes", abs(dorm_dict[name]), "Tomans.")
    print("Creditors:")
    for name in creditor_name:
        print(name, "paid", abs(dorm_dict[name]), "Tomans.")
