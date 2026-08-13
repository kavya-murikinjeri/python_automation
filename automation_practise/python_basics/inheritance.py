# inheritance allows a class to inherit all the attributes and methods from parent class
# helps with code reusability and extensibility

class RateOfInterest:
    interest =0.8 #class variable
    def __init__(self, name, loan):
        self.name=name  # instance variable
        self.loan=loan
    def calculate_interest(self):
        print("Total interest amount is: ",self.loan*self.interest)

class Student(RateOfInterest):
    interest = 0.7

std1=Student("kavya",50000)
std1.calculate_interest()
