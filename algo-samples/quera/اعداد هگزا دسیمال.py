user_input = input()
result = 0
l = len(user_input)
for i in user_input:
    if i > "1":
        result += 2**l-1
        break
    elif i == "1":
        result += 2**(l-1)
    l -= 1
print(result)

###
# test function
# n = int(user_input)
# count = 0
# for i in range(1, n+1):
#     if set(str(i)).issubset({"0", "1"}):
#         count += 1
# print(result, count)


##############
# score 86

# def loaded(inpt):
#     length = len(inpt)
#     result = 0
#     if length == 0 or inpt == "0":
#         return 0
#     if inpt[0] >= "1":
#         result += 2**(length-1)
#     return result + loaded(inpt[1:])


# print(loaded(user_input))
