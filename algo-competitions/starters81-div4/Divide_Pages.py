t = int(input())

for i in range(t):
    n = int(input())
    book_list = map(int, input().split())
    if sum(book_list) % 2 == 0:
        print("YES")
    else:
        print("NO")
