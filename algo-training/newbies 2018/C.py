number_of_arrays = int(input())
sets = []
for array_index in range(number_of_arrays):
    array_length = int(input())
    array_string = input().split(" ")
    array_int = [int(i) for i in array_string]
    sets += [set(array_int)]
    # smallest geometric mean in subests is smallest subsets of all
for item in sets:
    print("%.2f" % float(min(item)))

