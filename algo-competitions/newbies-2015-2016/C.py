n = int(input())
string_input = input().split(" ")
d = {}
score_dict = {}
for i in range(n):
    d[i+1] = sorted(string_input[i])
    score_dict[i+1] = 0
m = int(input())
io_list = []
for i in range(m):
    costumer = int(input())
    if costumer not in io_list:
        io_list.append(costumer)
    elif costumer in io_list:
        io_list.remove(costumer)
        for c in io_list:
            if d[costumer] == d[c]:
                score_dict[c] += 1
result = []
for i in range(n):
    result.append(score_dict[i+1])
print(" ".join(str(i) for i in result))
