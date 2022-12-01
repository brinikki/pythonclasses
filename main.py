class Pet:
  def __init__ (self, name, age, type):
    self.name = name
    self.age = age
    self.type = type
    
  def myfunc(self):
      #print("Hello my name is " + self.name)
    if self.type == "cat":
      print("meOW")
    elif self.type == "dog":
      print("WOOF")
    
    
my_object = Pet("Evan", 22, "cat")
my_object2 = Pet("Charles", 2, "dog")
#The self parameter is a reference to the current instance of the class
#print (my_object.name)
#print (my_object.age)
#print (my_object.name, 'is', my_object.age, 'years old')
my_object.myfunc()
my_object2.myfunc()