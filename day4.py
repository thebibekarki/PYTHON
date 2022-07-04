thisset = {"apple", "banana", "cherry"}
print(thisset)
#Set items are unordered, unchangeable, and do not allow duplicate values.
#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(len(thisset))
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1,set2,set3)
set4 = {"abc", 34, True, 40, "male"}
print(type(set4))
for x in thisset:
  print(x)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


print(thisdict["brand"])
thisdictt = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ("red", "white", "blue")
}

print(thisdictt)
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
a = 2
b = 330

print("A") if a > b else print("B")