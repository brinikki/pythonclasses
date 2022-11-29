class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
my_object = Person("Evan", 22)
#The self parameter is a reference to the current instance of the class
print (my_object.name)
print (my_object.age)
print (my_object.name, 'is', my_object.age, 'years old')


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
def myfunc(self):
  print("Hello my name is " + self.name)
my_object = Person("John", 36)
my_object.age = 40
my_object.myfunc()
print(my_object.age)
#You can delete an object with:
del my_object