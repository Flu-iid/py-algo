t = int(input())
for i in range(t):
    input_n_k = input().split(" ")
    n, k = int(input_n_k[0]), int(input_n_k[1])
    grades = []
    happinnes = []
    input_grades = input().split(" ")
    grades += [int(i) for i in input_grades]
    input_happiness = input().split(" ")
    happinnes += [int(i) for i in input_happiness]
    total = [(grades[i], happinnes[i]) for i in range(len(grades))]
    total.sort(key=lambda x: x[1], reverse=True)
    total_happiness = 0
    for i in total:
        if i[0] < 10:
            if k >= 10 - i[0]:
                change = 10 - i[0]
                total_happiness += i[1]
                k -= change
    print(total_happiness)
