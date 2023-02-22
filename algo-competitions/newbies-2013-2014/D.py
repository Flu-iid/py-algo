import math
t = int(input())
for i in range(t):
    m, t, b = [int(i) for i in input().split(" ")]
    h = m/t
    needed_slice = h*b
    pizza_count = math.ceil(needed_slice/8)
    slice_count = pizza_count * 8
    h_prime = math.floor(m/t)
    extra_slice = slice_count-h_prime*b
    maximum = h_prime + extra_slice
    print(pizza_count, maximum)
