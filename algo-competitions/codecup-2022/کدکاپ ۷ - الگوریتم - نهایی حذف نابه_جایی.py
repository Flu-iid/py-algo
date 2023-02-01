import random, math

# algo 2

def all_outcomes(a_max):
    all_possible_outocomes = math.factorial(a_max)
    count = 0
    li = []
    while (count < all_possible_outocomes):
        new_list = random.sample(range(1,a_max+1),a_max)
        if new_list not in li:
            li.append(new_list)
            count+=1
    return li

def mechanism(list):
    if len(list) == 0:
        return True
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            del list[i:i+2]
            return mechanism(list)
    return False
    

def main(n):
    all_outcomes_list = all_outcomes(n)
    count = sum([(mechanism(li)) for li in all_outcomes_list])
    return count%(10**9+7)

print(main(500))
# print(([(i>2) for i in range(10)]))
# print(random.sample(range(1,5),4))


