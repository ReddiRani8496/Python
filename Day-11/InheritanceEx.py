class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def print_data(self):
        print(f"Name: {self.firstname} {self.lastname}")


# p1 = Person("rekha","G");
# p1.print_data()

class Student(Person):

    def __init__(self,fname,lname,age):
        super().__init__(fname,lname)
        print(self.firstname,"from student constructor");
        self.age=age;
    def print_data(self):
        print("student method")

    def print_age(self):
        print(f"Age: {self.age}")

s1 = Student("rahul","ksd",30)

print(s1.firstname)

s1.print_data()

s2 = Student("skdj","dsjlkf",29);

s2.print_data()

print(s2.age)

# p1 = Person("rekha","rka");
# print(p1.age)

s2.print_age()

