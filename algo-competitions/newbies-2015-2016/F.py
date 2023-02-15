t = int(input())
for i in range(t):
    string_input = input().split(" ")
    n, m = int(string_input[0]), int(string_input[1])
    x_list = []
    for j in range(m):
        string_input2 = input().split(" ")
        a, b = int(string_input2[0]), int(string_input2[1])
        if 1 <= a <= n and 1 <= b <= n and a != b and ([a, b] not in x_list) and ([b, a] not in x_list):
            x_list.append([a, b])
    friend_list = []
    count = 0
    for item in x_list:
        if 1 in item:
            item.remove(1)
            friend_list.append(item[0])
            x_list.remove(item)
    for friend in friend_list:
        for item in x_list:
            if friend in item:
                count += 1
    print(count)
