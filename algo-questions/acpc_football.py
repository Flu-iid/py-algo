# input_scores = tuple(sorted([int(i) for i in input().split()]))
# # team_correalational_score
# t0 = []
# t1 = []
# t2 = []
# t3 = []
# scores = [(3, 0), (1, 1), (0, 3)]
# # games = [((t0, t1), (t2, t3)), ((t0, t2), (t1, t3)), ((t0, t3), (t1, t2))]
# # games = [matches 0, matches 1, ...] -> matches = ((match0),(match1))
# # round1 01
# tmp_0 = 0
# tmp_1 = 0
# tmp_2 = 0
# tmp_3 = 0
# for a, b in scores:
#     tmp_0 += a
#     tmp_1 += b
#     # round1 23
#     for c, d in scores:
#         tmp_2 += c
#         tmp_3 += d
#         # round2 02
#         for e, f in scores:
#             tmp_0 += e
#             tmp_2 += f
#             # round2 13
#             for g, h in scores:
#                 tmp_1 += g
#                 tmp_3 += h
#                 # round3 03
#                 for i, j in scores:
#                     tmp_0 += i
#                     tmp_3 += j
#                     # round3 12
#                     for k, l in scores:
#                         tmp_1 += k
#                         tmp_2 += l
#                         t0.append(tmp_0)
#                         t1.append(tmp_1)
#                         t2.append(tmp_2)
#                         t3.append(tmp_3)
#                         tmp_1 -= k
#                         tmp_2 -= l
#                     tmp_0 -= i
#                     tmp_3 -= j
#                 tmp_1 -= g
#                 tmp_3 -= h
#             tmp_0 -= e
#             tmp_2 -= f
#         tmp_2 -= c
#         tmp_3 -= d
#     tmp_0 -= a
#     tmp_1 -= b
# # print(tmp_0, tmp_1, tmp_2, tmp_3)

# memo = set()
# for i in range(len(t0)):
#     l = [t0[i], t1[i], t2[i], t3[i]]
#     l.sort()
#     memo.add(tuple(l))
# # print(memo)

# print("YES" if input_scores in memo else "NO")
# # print(t0, t1, t2, t3, sep="\n")


# #########################
# # scores = [9,6,3,0] # sorted
# # score = 3
# # if score == 3:
# #     pass


# ################
# # class NODE:
# #     def __init__(self) -> None:

############## first Solution ##################

t0 = []
t1 = []
t2 = []
t3 = []
scores = [(3, 0), (1, 1), (0, 3)]


# for first run to save memo
tmp_0 = 0
tmp_1 = 0
tmp_2 = 0
tmp_3 = 0
for a, b in scores:
    tmp_0 += a
    tmp_1 += b
    # round1 23
    for c, d in scores:
        tmp_2 += c
        tmp_3 += d
        # round2 02
        for e, f in scores:
            tmp_0 += e
            tmp_2 += f
            # round2 13
            for g, h in scores:
                tmp_1 += g
                tmp_3 += h
                # round3 03
                for i, j in scores:
                    tmp_0 += i
                    tmp_3 += j
                    # round3 12
                    for k, l in scores:
                        tmp_1 += k
                        tmp_2 += l
                        t0.append(tmp_0)
                        t1.append(tmp_1)
                        t2.append(tmp_2)
                        t3.append(tmp_3)
                        tmp_1 -= k
                        tmp_2 -= l
                    tmp_0 -= i
                    tmp_3 -= j
                tmp_1 -= g
                tmp_3 -= h
            tmp_0 -= e
            tmp_2 -= f
        tmp_2 -= c
        tmp_3 -= d
    tmp_0 -= a
    tmp_1 -= b


memo = set()
for i in range(len(t0)):
    l = [t0[i], t1[i], t2[i], t3[i]]
    l.sort()
    memo.add(tuple(l))
print(memo)


# after first run. now save memo from terminal output

memo = {(4, 4, 4, 4), (0, 3, 6, 9), (2, 2, 4, 7), (2, 4, 4, 6), (1, 3, 5, 5), (3, 4, 4, 5), (1, 3, 6, 7), (1, 2, 4, 9), (1, 4, 5, 5), (2, 2, 5, 5), (0, 3, 7, 7), (1, 3, 4, 9), (3, 3, 3, 3), (3, 3, 3, 9), (0, 4, 6, 7), (1, 2, 5, 7), (2, 2, 2, 9), (2, 4, 4, 5), (1, 3, 5, 7), (3, 4, 4, 4),
        (2, 3, 4, 5), (1, 4, 6, 6), (1, 1, 6, 9), (0, 4, 4, 9), (3, 3, 4, 7), (0, 5, 5, 5), (2, 2, 3, 7), (2, 3, 4, 7), (2, 3, 3, 5), (3, 4, 4, 6), (0, 6, 6, 6), (1, 4, 5, 6), (0, 4, 5, 7), (1, 1, 7, 7), (3, 3, 6, 6), (2, 2, 5, 6), (1, 3, 4, 7), (2, 3, 5, 5), (1, 4, 4, 7), (1, 2, 6, 7)}
input_scores = tuple(sorted([int(i) for i in input().split()]))
print("Valid Standings" if input_scores in memo else "Invalid Standings")
# print(len(memo))
