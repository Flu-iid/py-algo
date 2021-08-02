word1=input("word> ")
word2=input("reverse_word> ")

def is_reverse(a, b):
 if len(a)==len(b):
  i=0
  j=len(b)-1
  for i in range(len(a)):
   if a[i]==b[j]:
    print(f"{a[i]} : {b[j]}")
    j-=1
   else:
    print("character Error")
    return -1
  
  print("They are reverse!")
  return True
  
 else:
  print("length Error")
  return False


is_reverse(word1, word2)