# fib
# def fib(n, true_memo={0: 0, 1: 1}):
#     if n not in true_memo:
#         true_memo[n] = fib(n-1, true_memo) + fib(n-2, true_memo)
#     return true_memo[n]


# print(fib(35))


# tribonacci
# def tribonacci(n, true_memo={0: 0, 1: 0, 2: 1}):
#     if n not in true_memo:
#         true_memo[n] = tribonacci(n-1, true_memo) + tribonacci(n-2,
#                                                      true_memo) + tribonacci(n-3, true_memo)
#     return true_memo[n]


# print(tribonacci(37))


# def sum_possible(amount, numbers):
#     if amount == 0 or 1 in numbers:
#         return True
#     l = sorted(set(numbers), reverse=True)
#     true_memo = set([0])
#     tmp = amount
#     index = 0
#     effect_index = 0
#     #
#     while effect_index < len(l):
#         if tmp in true_memo:
#             return True
#         if index == len(l):
#             tmp = amount
#             effect_index += 1
#             index = effect_index
#         elif l[index] > tmp:
#             index += 1
#         else:
#             tmp -= l[index]
#     return False


# print(sum_possible(8, [5, 12, 4]))
# print(sum_possible(15, [6, 2, 10, 19]))
# print(sum_possible(14, [5, 2]))
# print(sum_possible(13, [3, 5]))


# sum_possible recursion

# def sum_possible(amount, numbers, memo={}):
#     l = sorted(set(numbers))
#     if amount == 0 or 1 in l:
#         return True
#     if amount < 0:
#         return False
#     for n in l:
#         if sum_possible(amount-n, l, memo):
#             memo[amount] = True
#             return True
#     memo[amount] = False
#     return False


# print(sum_possible(8, [5, 12, 4]))
# print(sum_possible(15, [6, 2, 10, 19]))
# print(sum_possible(14, [5, 2]))
# print(sum_possible(13, [3, 5]))


# min_change

# def min_change(amount, numbers, memo={}, step=0):
#     if amount == 0:
#         memo.setdefault(amount, step)
#         return step
#     l = sorted(set(numbers))
#     for n in l:
#         if min_change(amount-n, l, memo, step+1) >= 0:
#             memo.setdefault(amount-n, step+1)
#             return step+1
#         else:
#             return -1
#     return min(memo.values())


# print(min_change(8, [1, 5, 4, 12]))
# print(min_change(271, [10, 8, 265, 24]))


def sum_possible(amount, numbers, memo={}):
    pass


print(sum_possible(8, [5, 12, 4]))
print(sum_possible(15, [6, 2, 10, 19]))
print(sum_possible(14, [5, 2]))
print(sum_possible(13, [3, 5]))
