import random
import math

a=random.randint(0, 10)
x=int(input("x> "))
precision=int(input("accuaracy> "))

print(f"a is {a}\n  with sqrt> {math.sqrt(a)}")


epsilon=10**-precision

t=0

while True:
  y=(x+a/x)/2
  t+=1
  if abs(y-x)<epsilon:
    print(f"  with x   > {x}\nwith {t} times doing function")
    break
  else:
    x=y