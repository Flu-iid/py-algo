def mechanism(li):
    a, b, r = li[0], li[1], li[2]
    q = (a-r) / b
    if b == 0 and a == r:
        print("Yes")
    elif 0<=a<=100 and 0<=a<=100 and 0<b<=100 and int(q)==q :
        print("Yes")
    else:
        print("No")

def main():
    number_of_tries = int(input())
    final_list = []
    if 1<=number_of_tries<=100:
        for i in range(number_of_tries):
            input_string = input()
            input_list_string = input_string.split(" ")
            input_list = [int(i) for i in input_list_string]
            final_list+=[input_list]
        [mechanism(item) for item in final_list]

main()