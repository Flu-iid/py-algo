import math


in_value=int(input("math.pi accuaracy> "))


def factorial(a):
 n=1
 for i in range(1, a+1):
  n=n*i
 return n

#or use math.factorial


def func_inloop(k):
 return (factorial(4*k)*(1103+26390*k))/((factorial(k)**4)*(396)**(4*k))


def inloop(k):
 for i in range(k):
  return func_inloop(i)
 

def my_pi(k):
 return (9801)/((2*math.sqrt(2))*(inloop(k)))


def result(k):
  print(f"my_pi   > {my_pi(k)}\nmath.pi > {math.pi}")



result(in_value)