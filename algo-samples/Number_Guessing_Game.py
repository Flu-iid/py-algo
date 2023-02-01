import random
a = random.randrange(0, 10)

print ('''Welcome to the guessing game!
Numbers are from 0 to 9 and you have 3 chance to get the number
Goodluck!
''')

t = 0

while t != 3 :
    b = int(input("Guess me: "))
    if abs(a-b) > 2 :
        print ("Too Far!")
    elif abs(a-b) == 0 :
        break
    else :
        print ("Close!")
    t = t + 1


if a == b:
    print ("You Won!")
    print ("I was " + str(a))
else:
    print ("You Lost :(")
    print ("I was " + str(a))
