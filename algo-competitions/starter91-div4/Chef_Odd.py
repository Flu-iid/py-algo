for _ in range(int(input())):
    n, k = map(int, input().split())
    if n < k*2:
        print("NO")
    else:
        odd_count = n//2 if not n % 2 else n//2+1
        # if even / if odd
        odd_count -= k
        if not odd_count % 2:
            # if remain odd_count even
            print("YES")
        else:
            print("NO")
