# class is a blueprint used to design the structure and layout of an object
class Employee:
    def __init__(self,fname,lname,email):
        self.fname=fname
        self.lname=lname
        self.email=email

    def greetEmployee(self):
        print(f"Hello! {self.fname}, Welcome to the class")
emp1=Employee("kavya","Murikinjeri","kavya@gmail.com")
emp2=Employee("Surya","N","surya@gmail.com")
print(emp1.fname)
emp1.greetEmployee()
    
        