#reverse step method palindrome

word=input("Lets check if its palindrome> ")

def remain(a):
 return a[1:-1]

def r_palindrome(a):
 for i in range(len(a)):
  b=a[::-1]
  if i<=1 and a==b:
   print("Its palindrome!")
   return True
  elif a[i]==b[i]:
   a=remain(a)
  elif a[i]!=b[i]:
   print("It isnt palindrome")
   return -1
  else:
   print("Error")
   return False

r_palindrome(word)