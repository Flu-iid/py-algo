t = int(input())
for i in range(t):
    string_input = input().split(" ")
    n, m = [int(i) for i in string_input]
    crush_graph = []
    for i in range(m):
        string_input2 = input().split(" ")
        u, v = [int(i) for i in string_input2]
        if u != v and 1 <= u <= n and 1 <= v <= n:
            crush_graph.append([u, v])
    print(crush_graph)
    n_list = list(range(1, n+1))
    print(n_list)
    for crush in crush_graph:
        for f in n_list:
            if f not in crush[0]:
