user_input = input()
count = user_input.count("?")
binary_possible = format(2**count-1, f"0{count}b")
while binary_possible != format(-1, f"0{count}b"):
    answer = user_input
    for i in range(count):
        answer = answer.replace("?", binary_possible[i], 1)
    print(answer)
    binary_possible = format(int(binary_possible, 2)-1, f"0{count}b")
