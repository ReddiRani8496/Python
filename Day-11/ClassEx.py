class Person:

  def __init__(self, name, age):

    self.name = name

    self.age = age
  
  def __str__(abc):

    return f"Person: {abc.name}, Age: {abc.age}"



p1 = Person("John", 36)

print(p1)



print(p1.name)  #john

del p1

print(p1.age) #36
print(p1.name)


p2 = Person("Nick", 26)

print(p2.name) #nick

print(p2.age) #26

p1.name="rock"

print(p1.name) 
