from time import time
import os
from string import printable, digits
# printable = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '	', '\n', '\r', '', '']


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


def encrypt(input_string, rot=13):
    """
    add rotation to ascii number
    """
    if os.path.exists("./config.txt"):
        with open("config.txt", "r") as fin:
            content = fin.read()
            key = content.find("rot=")
            if key >= 0:
                value = content[4:].strip()
                rot = value
    else:
        while True:
            print("no config file found, do you want to make a key?(Y/n)")
            key_answer_input = input(">").lower()
            if key_answer_input in ["yes", "y", "yeah"]:
                user_input = input("enter rotation integer >").lower()
                if user_input not in digits:
                    print("bad input. try again.")
                else:
                    rot = int(user_input)
                    with open("config.txt", "w") as fin:
                        fin.write(f"rot={rot}")
                        break
            elif key_answer_input in ["no", "n", "nope"]:
                print("ok, try to remember it then!")
                break
            else:
                print("bad input. try again.")
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

if __name__ == "__main__":
    pass
