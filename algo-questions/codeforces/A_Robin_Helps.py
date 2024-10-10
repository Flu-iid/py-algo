def main(n, k, array:list):
    bag = 0
    count = 0
    for i in array:
        if i>=k:
            bag+= i
        elif i==0 and bag>0:
            bag -= 1
            count += 1
    
    return count


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        gold_array = [int(i) for i in input().split()]
        ans = main(n, k, gold_array)
        print(ans)