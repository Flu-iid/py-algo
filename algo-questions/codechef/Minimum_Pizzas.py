for _ in range(int(input())):
    n, x = map(int, input().split())
    slice_count = n*x
    pizza_count = slice_count//4
    extra_pizza = 1 if slice_count % 4 else 0
    print(pizza_count+extra_pizza)
