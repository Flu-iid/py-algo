from time import time
import os
# from string import printable
printable = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '	', '\n', '\r', '', '']


# read config if availabe, if not make one
# with open("config.txt", "r") as fin:
#     fin.readlines()

config = 13


# add utc in between and fill in the gaps with the same result


def ascii_printable(s):
    """
    printable ascii charecters
    """
    for c in s:
        if c not in printable:
            return False
    return True


def number_to_base(n, b):
    """
    turn base10 number to any base number
    """
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def encrypt(input_string, rot=config):
    """
    add rotation to ascii number
    """
    if ascii_printable(input_string):
        t_data = time()
        rot_list = [(printable.index(c)+rot) % len(printable)
                    for c in input_string]
        encrypt_result = ""
        delimiter = "/"

        for r in rot_list:
            encrypt_result += str(t_data*7/10)+delimiter + \
                str(r*100/97+1)+delimiter+str(r*100/97-1)
        encrypt_result += str(len(rot_list))+delimiter+str(t_data*7/10)
        return encrypt_result
    else:
        print("Bad input")
        return 1


# print(encrypt("Arsham Mahdiun"))

with open("output.txt", "a+") as fin:
    print(fin.readable())
# print(int("1000", 2))
# print(number_to_base(8, 2))
