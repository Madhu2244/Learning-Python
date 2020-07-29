#Empty Class
class Employee:
    pass

#creating objects
emp1 = Employee()
emp2 = Employee()

emp1.fname = "Madhu"
emp1.lname = "Sharma"
print(emp1.fname + " " + emp1.lname)

#Initializing or using a constructor
class Employee:

    extension = "@emp.com"
    #self is the reference to the instance itself ("this" keyword in java)
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.name = fname + " " + lname

    def intro(self):
        print("My name is " + self.name)

    def emailid(self):
        print("I can be reached at " + self.fname + "_" + self.lname + Employee.extension)

emp1 = Employee("Madhu", "Sharma")
print(emp1.emailid())