for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    d = dict()
    for i in range(n):
        if b[i] <= 0:
            continue
        if a[i] not in d.keys():
            d[a[i]] = b[i]
        else:
            if b[i] > d[a[i]]:
                d[a[i]] = b[i]
    # print(d)
    sum = 0
    while d.keys():
        choice = list(d.keys())[0]
        sum += d[choice]
        del d[choice]
    print(sum)

    # missunderstood.. though shouldnt have 2 types next to eachother
    # for i in range(len(a)):
    #     if b[i] <= 0:
    #         continue
    #     if a[i] in d.keys():
    #         d[a[i]] += [b[i]]
    #     else:
    #         d[a[i]] = [b[i]]
    # if not d.keys():
    #     print(0)
    # else:
    #     choices = list(d.keys())
    #     choice = list(d.keys())[0]
    #     sum = 0
    #     while True:
    #         choices.remove(choice)

    #         choice_value = max(d[choice])
    #         sum += choice_value
    #         d[choice].remove(choice_value)

    #         if not d[choice]:
    #             del d[choice]

    #         if not d.keys() or not choices:
    #             print(sum) if sum >= 0 else print(0)
    #             break

    #         choice = choices[0]
