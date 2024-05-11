t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())

    cnt_a = 0
    cnt_c = 0

    for i, char in enumerate(s):
        if char == "b":
            before = False
            after = False
            tmp_a = set()
            tmp_c = set()
            for i_a, a in enumerate(s[:i]):
                if a == "a":
                    before = True
                    tmp_a.add(i_a)
            for i_c, c in enumerate(s[i + 1 :]):
                if c == "c":
                    after = True
                    tmp_c.add(i_c + i + 1)

            if before and after:
                for e in tmp_a:
                    s[e] = "0"
                for e in tmp_c:
                    s[e] = "0"
                cnt_a += len(tmp_a)
                cnt_c += len(tmp_c)

    result = 0
    if cnt_a and cnt_c:
        result = min(cnt_a, cnt_c)

    print(result)


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()

#     a_set = set()
#     c_set = set()

#     for i, char in enumerate(s):
#         if char == "b":
#             before = False
#             after = False
#             tmp_a = set()
#             tmp_c = set()
#             for i_a, a in enumerate(s[:i]):
#                 if a == "a":
#                     before = True
#                     tmp_a.add(i_a)
#             for i_c, c in enumerate(s[i + 1 :]):
#                 if c == "c":
#                     after = True
#                     tmp_c.add(i_c + i + 1)

#             if before and after:
#                 a_set |= tmp_a
#                 c_set |= tmp_c

#     result = 0
#     if a_set and c_set:
#         result = min(len(a_set), len((c_set)))

#     print(result)
