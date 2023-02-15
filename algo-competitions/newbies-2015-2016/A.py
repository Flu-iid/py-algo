import math

t = int(input())
for i in range(t):
    string_input = input().split(" ")
    r, w, l = int(string_input[0]), int(string_input[1]), int(string_input[2])
    if math.sqrt(w**2+l**2)/2 <= r:
        print("Pizza fits on the table.")
    else:
        print("Pizza does not fit on the table.")
