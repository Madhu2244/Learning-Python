'''#Empty Class
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

    extension = "@emp.com" #class variable
    #self is the reference to the instance itself ("this" keyword in java)
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.name = fname + " " + lname

    @property #To decalre a method as a get method --> keyword @property
    def intro(self):
        return("My name is " + self.name + " " + self.lname)

    @intro.setter #@functionname.setter
    def intro(self,name):
        fname,lname = name.split(' ')
        self.fname = fname
        self.lname = lname
        print("My name is " + self.fname + " "+ self.lname)
    def emailid(self):
        return("I can be reached at " + self.fname + "_" + self.lname + Employee.extension)

    @classmethod #decorators
    def email_update(cls,ext): #This is a class method
        cls.extension =ext

    @classmethod #cls means it takes in the class
    def from_name(cls,info):
        fname, lname = info.split('-') #info is what is passed into the parameters
        return cls(fname,lname)

    @staticmethod #non changing compared to dynamic #can be used with any object, not a method for the object, but for the class
    def comp_name():
        return("I work at Python_Academy")

#Inheritence
class developer(Employee):
    #parent constructor is created before the child constructor.
    def __init__(self,fname,lname,language = None):
        # inheritence from employee class, it is going to search for this constructor fname,lname. #Object - from which all classes are inherintin
        super().__init__(fname,lname)
        if language is None:
            self.language = "Not Mapped Yet"
        else:
            self.language = language
    #magic method (like rewrting toString)
    def __repr__(self):
        return "Developer : Fname - '{}', lname - '{}', language - '{}'".format(self.fname,self.lname,self.language)
    def __str__(self):
        return '{} - {}'.format(self.name,self.emailid())
    def __add__(self, other):
        pass
    def __len__(self):
        return len(self.name)


emp1 = Employee("Madhu", "Sharma")
emp1.intro()
emp1.emailid()
emp2 = Employee.from_name("Ryan-Jones")
emp2.intro()
emp2.emailid()
Employee.email_update("@python.org")
emp2.emailid()

dev1 = developer("Madhu","Sharma","Python")
print(dev1.intro())
print(help(developer))

#check if an object is an instance of a class
print(isinstance(dev1,developer)) #object mentioned as parameter 1 is an instance of class mentioned in parameter 2
print(isinstance(dev1,Employee)) #True because
#check if a class is a subclass of another
print(issubclass(developer,Employee))
print(issubclass(Employee,developer))
#Magic methods or Dunder methods --> used for operator overloading
print()
dev1.__str__()
print(dev1.__repr__())
print(dev1.__len__())
print(dev1.name)
print(dev1)'''

class Car:
    def __init__(self,wheels,doors,trunk,HorsePower,Gears,Mileage,Price,Date,carModel):
        self.wheels = wheels
        self.doors = doors
        self.trunk = trunk
        self.HorsePower = HorsePower
        self.Gears = Gears
        self.Mileage = Mileage
        self.Price = Price
        self.Date = Date
        self.carModel = carModel

    def carType(self, carModel):
        self.carModel = carModel

class Mercedes(Car):
    company = "Mercedes"
    def __init__(self,wheels,doors,trunk,HorsePower,Gears,Mileage,Price,Date,carModel = None):
        super().__init__(self,wheels,doors,trunk,HorsePower,Gears,Mileage,Price,Date)
        if carModel == None:
            self.carModel = "Not Mapped Yet"
        else:
            self.carModel = carModel

class Jaguar(Car):
    company = "Jaguar"
    def __init__(self,wheels,doors,trunk,HorsePower,Gears,Mileage,Price,Date,carModel = None):
        super().__init__(self,wheels,doors,trunk,HorsePower,Gears,Mileage,Price,Date)
        if carModel == None:
            self.carModel = "Not Mapped Yet"
        else:
            self.carModel = carModel
class Bentley(Car):
    company = "Bentley"
    def __init__(self, wheels, doors, trunk, HorsePower, Gears,Mileage, Price, Date, carModel=None):
        super().__init__(self, wheels, doors, trunk, HorsePower, Gears,Mileage, Price, Date)
        if carModel == None:
            self.carModel = "Not Mapped Yet"
        else:
            self.carModel = carModel

merc1 = Mercedes(4,4,True,400,6,24.6,20000,"07-29-2020")

print(merc1)
merc1.carType("X-Series")
print(merc1.carModel)
