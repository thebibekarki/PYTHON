import random

x=(random.randrange(1, 10))

a=9
for i in range(1,10):
 y=input("Enter the desired number: ")
 if x ==int(y):
  print("CONGRATULATIONS....YOU HAVE GUESSED RIGHT NUMBER!!!!")
  break;
 else:
  a=a-1
  print("SORRY....TRY AGAIN!!!!!!")
  if(a==1):
    print("LAST TRY")
  else:
    print("YOU HAVE ",a," TRIES LEFT")
       
