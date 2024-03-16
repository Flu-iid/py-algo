def price_counter(l: list):
    if len(l) == 1:
        return l[0]
    if len(l) % 2:
        l.remove(max(l))
    even_index_items = [l[i] for i in range(0, len(l), 2)]
    odd_index_items = [l[i] for i in range(1, len(l), 2)]
    return min(sum(even_index_items), sum(odd_index_items))


for _ in range(int(input())):
    n = int(input())
    price = [int(i) for i in input().split()]
    print(price_counter(price))
