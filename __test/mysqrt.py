import math

def my_sqrt(number):
    x=number/2
    while True:
        root_esitmation = (number/x + x)/2
        if root_esitmation==x:
            return root_esitmation
        x = root_esitmation


if __name__ == "__main__":
    space = 25
    max_num = int(input(">"))
    titles = ["a", "sqrt", "my_sqrt", "diff"]
    title = ""
    for t in titles:
        title+=t+" "*(space-len(t))
    print(title)
    # dash row
    for c in title:
        if c!=" ":
            print("-", end="")
        else:
            print(" ",end="")
    print()
    # numbers row
    for i in range(1,max_num+1 ):
        print(str(i)+" "*(space-len(str(i))), end="")
        math_sqrt = math.sqrt(i)
        print(str(math_sqrt)+" "*(space-len(str(math_sqrt))), end="")
        my_square_root = my_sqrt(i)
        print(str(my_square_root)+" "*(space-len(str(my_square_root))),end="")
        diff = abs(math_sqrt-my_square_root)
        print(str(diff)+" "*(space-len(str(diff))))



