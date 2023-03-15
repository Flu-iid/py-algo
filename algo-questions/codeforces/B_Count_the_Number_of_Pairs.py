# t = int(input())


# def check(c, d):
#     return (c.lower(), c.upper()) in d


# for i in range(t):
#     n, k = map(int, input().split(" "))
#     s = input()

#     d = {}

#     for c in s:
#         if not check(c, d):
#             d[(c.lower(), c.upper())] = [0, 0]
#         if c == c.lower():
#             d[(c.lower(), c.upper())][0] += 1
#         else:
#             d[(c.lower(), c.upper())][1] += 1

#     base_score, k_score, allowed_k = 0, 0, k
#     for key in d:
#         base_score += min(d[(key)])
#         possible_extra = int(abs(d[key][0]-d[key][1])//2)
#         if possible_extra <= allowed_k and possible_extra > 0:
#             k_score += possible_extra
#             allowed_k -= possible_extra
#         elif possible_extra > allowed_k:
#             k_score += allowed_k
#             allowed_k = 0
#             break
#     print(base_score+k_score)


t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    s = input()

    d = {}
    for c in s:
        key = (c.lower(), c.upper())
        d.setdefault(key, [0, 0])
        if c == c.lower():
            d[key][0] += 1
        else:
            d[key][1] += 1

    base_score = 0  # base score is min number for each pair
    extra_score = 0  # extra score is floor of div/2 of each pair
    for key in d:
        base_score += min(d[key])
        extra_score += int(abs(d[key][1]-d[key][0])/2)

    if extra_score >= k:
        print(base_score+k)
    else:
        print(base_score+extra_score)

    # print("base: ", base_score, "extra: ", extra_score, "k: ", k)
