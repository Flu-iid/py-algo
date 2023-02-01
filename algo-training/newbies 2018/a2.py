number_of_tries = int(input())
answers = []
for i in range(number_of_tries):
    input_string = input()
    input_list_string = input_string.split(" ")
    input_list = [int(i) for i in input_list_string]
    a, b, r = input_list[0], input_list[1], input_list[2]
    if b == 0:
        answers += ["Yes"]
        continue
    q = (a-r) / b
    if 0<=a<=100 and 0<b<=100 and 0<=r<=100 and int(q)==q :
        answers += ["Yes"]
    else:
        answers += ["No"]

[print(i) for i in answers]




