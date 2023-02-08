t = int(input())
for i in range(t):
    input_string = input().split(" ")
    n, m = int(input_string[0]), int(input_string[1])
    if m == 0:
        print(n % 10)
    else:
        # cause 245 to power of every number bigger than zero will have least significant digit of 5
        print(n*5 % 10)
