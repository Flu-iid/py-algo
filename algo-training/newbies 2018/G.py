t = int(input())

def str_to_int_list(s):
    return list(map(int, s))

def int_list_to_str(li):
    return "".join([str(i) for i in li])

answer = []

for i in range(t):
    imei = input()
    imei_list = str_to_int_list(imei)
    tac_list = imei_list[0:8]
    tac = int_list_to_str(tac_list)
    imei_list_x2 = []
    for i in range(len(imei_list)):
        if i%2==0:
            imei_list_x2+=[imei_list[i]]
        else:
            imei_list_x2+=[imei_list[i]*2]
    imei_list_x2_str = int_list_to_str(imei_list_x2)
    imei_list_x2_new = str_to_int_list(imei_list_x2_str)
    checksum = 10 - sum(imei_list_x2_new)%10
    answer += [[tac, checksum]]

for i in answer:
    print(i[0]," ",i[1])
    

