"""
This function will theme input string with sql-shape squares
"""

def square(user_input="#"):
    str_list = list(user_input)
    str_length = len(str_list)
    #dash row
    print("+", end="")
    print(" - - - +" * str_length)
    #space row
    print("|", end="")
    print("       |" * str_length)
    #char row
    print("|", end="")
    for char in str_list:
        print(f"   {char}   |", end="")
    print()
    #space row
    print("|", end="")
    print("       |" * str_length)
    #dash row
    print("+", end="")
    print(" - - - +" * str_length)

if __name__ == "__main__":
    user_input = input("str input > ")
    if user_input:
        square(user_input)