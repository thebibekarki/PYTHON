"""print("hello world")
if 5>2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")
for x in range(1,6):
    print(x)

x="bibek"
print(x)
#fruits = ["apple", "banana", "cherry","mango"]
#x, y, z, a= "apple", "banana", "cherry","mango"
x= y= z= a= "apple"
print(x)
print(y)
print(z)
print(a)"""

X= "awesome"

def myfunc():
  global X
  X= "fantastic"
  print("Python is ",X)

myfunc()


print("Python is ",X)
