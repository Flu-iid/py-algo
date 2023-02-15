n = int(input())
string_input = input().split(" ")
parsa_li = [float(i) for i in string_input]
if len(parsa_li) == 1:
    print("{:.5f}".format(0))
else:
    for count in range(n):
        i = n - 1 - count
        if i == 0:
            ans = ""
            for item in parsa_li:
                ans += "{:.5f}".format(item) + " "
            print(ans)
            continue
        quant = parsa_li[i]/i
        for item_i in range(len(parsa_li[:i])):
            parsa_li[item_i] += quant
