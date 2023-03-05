d = {"s": 1, "o": 10, "a": 100}
rule_set = {"s", "o", "a"}
result = {}
for i in rule_set:
    for j in rule_set:
        for k in rule_set:
            item = (d[i], d[j], d[k])
            if sum(item) != 30:
                if sum(item) not in result:
                    result[sum(item)] = (i, j, k)

print(result, len(result))
