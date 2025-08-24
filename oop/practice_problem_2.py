class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self)    :
        return f"{self.name} is {self.age} years old"
class Student(Person)  :
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)      
        self.roll_no = roll_no
    def info(self):
        print(f"{self.name},{self.age} , {self.roll_no}") 
a = Student('Sam',16,46)
a.info()        
