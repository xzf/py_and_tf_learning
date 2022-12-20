
x = float(5)
y = float(2)
print(y ** x)
print(x // y)
print(x / y)
if x<y:
 print(x,"<",y)
elif x==y:
   print(x,"=",y)
else:
 print(x,">",y)

if x<y: print(x,"<",y)
elif x==y:  print(x,"=",y)
else: print(x,">",y)
"""
???????
???
???
"""
z = 1j
print(z)
z = -87.7e100
print(z)
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(len(thisset))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(len(thisdict))
print(thisdict["year"])

i = 1
while i < 4:
  print("while "+str(i))
  i += 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
for x in range(2, 11, 2):
  print(x)
def my_function():
  print("Hello from a function")

my_function()

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function()

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(2)
print(mytripler(2))

array = ["1", "2", "2"]
print(array)
print(len(array))
print(array.count("2"))
array[2]="3"
print(array)
array.append("4")
print(array)
array.pop(3)
print(array)
array.remove("3")
print(array)
array.reverse()
print(array)
array.sort()
print(array)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return self.name+" "+str(self.age)

p1 = Person("John", 36)
print(p1)

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))