t = int(input())
for i in range(t):
    string_input = input().split(" ")
    n, m = int(string_input[0]), int(string_input[1])
    x_set = set()
    for i in range(m):
        string_input2 = input().split(" ")
        a, b = int(string_input2[0]), int(string_input2[1])
        if 1 <= a <= n and 1 <= b <= n and a != b:
            if a < b:
                x_set.add((a, b))
            else:
                x_set.add((b, a))
    friend_list = []
    x1_set = set()
    count = 0
    for item in x_set:
        if 1 in item:
            friend_list.append(item[1])
            x1_set.add(item)
    print(x_set, x1_set)
    x_final_set = x_set.difference(x1_set)
    print(x_final_set, x_set, x1_set)
    for item in x_final_set:
        if item[0] in friend_list:
            count += 1
    print(count)
