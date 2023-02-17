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
    d = []
    while n:
        d.append(int(n % b))
        n //= b
    return d[::-1]


def ascii_encrypt(input_string, rot=13):
    """
    add rotation to ascii number
    """
    if input_string:
        t_data = time()
        rot_list = [(ord(c)+rot) % len(printable)
                    for c in input_string]
        encrypt_result, delimiter, spacer = "", "☺", "☻"

        for r in rot_list:
            r_p = str(r*100/97+1)
            r_m = str(r*100/97-1)
            if len(r_p) < 17:
                r_p += spacer * (17-len(r_p))
            if len(r_m) < 17:
                r_m += spacer * (17-len(r_p))

            encrypt_result += str(t_data*7/10)+delimiter + \
                r_p+delimiter+r_m
        encrypt_result += str(len(rot_list))+delimiter+str(t_data*7/10)
        return encrypt_result
    else:
        print("Bad input")
        return 0


def user_answer():
    """
    yes/no answer check. yes, no, bad = "y", "n", False
    """
    key_answer_input = input(">").lower()
    if key_answer_input in ["yes", "y", "yep", "yeah"]:
        return "y"

    elif key_answer_input in ["no", "n", "nope", "nah"]:
        return "n"
    else:
        print("bad input. try again.")
        return False


def make_config(message):
    """
    make config for costume function
    """
    tmp_rot = 13
    while True:
        print(message)
        answer = user_answer()
        if answer == "y":
            user_input = input("enter rotation integer >").lower()
            if user_input not in digits:
                print("bad input. try again.")
            else:
                rot = int(user_input)
                tmp_rot = rot
                with open("config.txt", "w") as fin:
                    fin.write(f"rot={rot}")
                    break
        elif answer == "n":
            print("ok, try to remember it then!")
            user_input = input("enter rotation integer >").lower()
            tmp_rot = int(user_input)
            break
        else:
            pass
    return tmp_rot


def encrypt_type(func=ascii_encrypt, rot=13):
    """
    run encryption type by user command
    """
    print(func(input("data >"), rot))
    # ask for output save


# print(encrypt("Arsham Mahdiun"))
if __name__ == "__main__":
    if os.path.exists("config.txt"):
        with open("config.txt", "r") as fin:
            content = fin.read()
            key = content.find("rot=")
            if key >= 0:
                value = content[4:].strip()
                if value.isdigit():
                    # get encrypt type
                    encrypt_type(rot=int(value))
                else:
                    tmp_rot = make_config(
                        "bad config, do you want to make a key?(Y/n)")
                    # get encrypt type
                    encrypt_type(rot=tmp_rot)
    else:
        tmp_rot = make_config(
            "no config file found, do you want to make a key?(Y/n)")
        # get encrypt type
        encrypt_type(rot=tmp_rot)
