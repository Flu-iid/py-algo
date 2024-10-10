from functools import reduce

def main(n:int, array:list):
    array.sort()
    print(reduce(lambda a,b: (a+b)//2, array))





if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = [int(i) for i in input().split()]
        main(n, array)
