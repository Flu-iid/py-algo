t = int(input())
for i in range(t):
    string_input = input().split(" ")
    s, n = [int(i) for i in string_input]
    side = ([2, 4, 6, 8], 5)
    corner = ([1, 3, 7, 9], 5)
    center = ([5], 8)
    result = 1
    for i in range(n-1):

    print(f"Case#{i+1} : {result}")
