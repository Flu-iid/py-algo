# not complete

def main(n, x, array:list):
    array.sort()
    final_array:list = [-1]*(n+2)
    extra = []
    for i in array:
        if final_array[i]==-1:
            final_array[i]=i
        else:
            extra.append(i)
    
    empty_slots = [i for i in final_array if i==-1]

    mex = final_array.index(-1)

    for i in empty_slots:
        if not (mex-i)/x:
            final_array[mex]

    
            


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        array = [int(i) for i in input().split() if int(i)<=n]
        main(n, x, array)
