import math
import gamma

def my_sqrt(number):
    x=number/2
    while True:
        root_esitmation = (number/x + x)/2
        if root_esitmation==x:
            return root_esitmation
        x = root_esitmation


if __name__ == "__main__":
    gamma.title(range(1,13),[lambda i:i, math.sqrt, my_sqrt, lambda i:abs(math.sqrt(i)-my_sqrt(i))])


