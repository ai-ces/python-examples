
class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi olusturuldu")


class Student(Person):
    pass


class Teacher(Person):
    pass

p1 = Person("aaa","bbbb",30)
print(p1.name,p1.surname,p1.age)
s1 = Student("ccc","dddd","19")
print(s1.name,s1.surname,s1.age)