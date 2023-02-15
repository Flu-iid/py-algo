t = int(input())
for i in range(t):
    n = int(input())
    x_all = []
    y_all = []
    v_x_all = []
    v_y_all = []
    for i in range(n):
        string_input = input().split(" ")
        x, y, v_x, v_y = [float(i) for i in string_input]
        x_all.append(x)
        y_all.append(y)
        v_x_all.append(v_x)
        v_y_all.append(v_y)

    x_instance = sum(x_all)/n
