import math

t = int(input())
for i in range(t):
    input_string = input().split(" ")
    n, p, e = int(input_string[0]), int(input_string[1]), int(input_string[2])
    bisc_list = []
    for bisc in range(n):
        input_string_bisc = input().split(" ")
        input_string_bisc_int = [float(i) for i in input_string_bisc]
        input_string_bisc_int.sort()
        bisc_list.append(input_string_bisc_int[-1])
    for i in range(len(bisc_list)):
        if (p-e) <= (i+1)/len(bisc_list) <= (p+e):
            # bisc_list[i] = rad2 a
            edge = bisc_list[i]/math.sqrt(2)
            print("{:.2f}".format(round(edge, 2)))
        if i+1 == len(bisc_list):
            print("IMPOSSIBLE")

# dont know where is wrong
