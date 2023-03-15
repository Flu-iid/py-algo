# t = int(input())

def generateAllBinaryStrings(n, arr, i, result=set()):

    if i == n:
        result.add("".join(map(str, arr)))
        return result

    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1, result)
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1, result)


print(generateAllBinaryStrings(5, [None]*5, 0))


# for i in range(t):
#     n = int(input())
