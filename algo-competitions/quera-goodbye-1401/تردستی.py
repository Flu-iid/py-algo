t = int(input())

for _ in range(t):
    s = input()+"1"
    count = 0
    for i, el in enumerate(s):
        if el == "0" and s[i+1] == "1":
            count += 1
    print(count)
