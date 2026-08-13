# class variables shared among all the instances of the class and are defined outside the constructor
# class variables can be shared by all the objects of the class
#instance variables are declared inside init constructor

class RateOfInterest:
    interest =0.8 #class variable
    def __init__(self, name, loan):
        self.name=name  # instance variable
        self.loan=loan
    def calculate_interest(self):
        print("Total interest amount is: ",self.loan*RateOfInterest.interest)

cust1=RateOfInterest("kavya",10000)
cust1.calculate_interest()
RateOfInterest.interest=0.9
cust2=RateOfInterest("Surya",50000)
