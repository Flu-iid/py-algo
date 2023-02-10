input_string = input().split(" ")
n, m = int(input_string[0]), int(input_string[1])
input_array_n = input().split(" ")
array_n = [int(i) for i in input_array_n]
for i in range(m):
    input_cmd = input().split(" ")
    array_cmd = [int(i) for i in input_cmd]
    if array_cmd[0] == 1:
        a, b, k = array_cmd[1], array_cmd[2], array_cmd[3]
        i_a = array_n.index(a)
        i_b = array_n.index(b)
        array_n[i_a:i_b+1] = [i**k for i in array_n[i_a:i_b+1]]
    elif array_cmd[0] == 42:
        a, b = array_cmd[1], array_cmd[2]
        i_a = array_n.index(a)
        i_b = array_n.index(b)
        result = 1
        for i in array_n[i_a:i_b+1]:
            result *= i
        print(result % (10**9+7))


# bad read
