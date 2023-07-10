for _ in range(int(input())):
    n, q = map(int, input().split())
    # n length of array
    # q number of queries
    a = [int(i) for i in input().split()]
    # array
    query_index_dict = {}
    for i in range(n):
        query_index_dict.setdefault(i, 0)
    for i in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        for index in range(l, r+1):
            query_index_dict[index] += 1
    value_dict = {}
    for k in query_index_dict:
        v = query_index_dict[k]
        value_dict.setdefault(v, list())
        value_dict[v].append(k)
    new_array = [0 for i in range(n)]
    for i in range(n, 0, -1):
        max_val = max(value_dict.keys())
        for index in value_dict[max_val]:
            new_array[index] = i
        value_dict.pop(max_val)
    print(sum(new_array))
    print("".join(new_array))
