for _ in range(int(input())):
    n = int(input())
    s = input()
    x0, x1 = [], []
    x0.append("0")
    x1.append("1")
    for i in range(n-1):
        xor_x0 = int(x0[i]) ^ int(s[i])
        x0.append(str(xor_x0))
        xor_x1 = int(x1[i]) ^ int(s[i])
        x1.append(str(xor_x1))
    x0_count, x1_count = x0.count("1"), x1.count("1")
    print(max(x0_count, x1_count))
