import math
from pyclbr import Class


class Sport:
    def __init__(self, name, players):
        self.name = name
        self.players = players


volleyball = Sport("Volleyball", 6)
delete = Sport("Delete", 6)
print(volleyball.name)

print(delete.players)


class Robots:

    def __init__(self,name,age,tasks):
        self.name = name
        self.model = age
        self.tasks = tasks

Alexa = Robots("Alexa:   Hi, my name is Alexa", "Alexa:   I was created in 2015","Alexa:   I can play music, set alarms, and control smart home devices")
Sofia = Robots("Sofia:   Hi, my name is Sofia", "Sofia:   I was created one year after you were created, in 2016","Sofia:   I can have conversations, recognize faces, and express emotions")        

print(Alexa.name)
print(Sofia.name)
print(Alexa.model)
print(Sofia.model)  
print(Alexa.tasks)
print(Sofia.tasks)

class number:
    def __init__(self, num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def add(self,num1,num2,num3):
        return self.num1 + self.num2 + self.num3


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

numb = number(num1, num2, num3)
print(numb.add(numb.num1, numb.num2, numb.num3))



#Parent class
class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber 
    def display(self):
        print(self.name)
        print(self.idnumber)
name = input("Enter your name: ")
idnumber = input("Enter your ID number: ")        
   

#Child class
class Employees(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post


        #invoking the __init__ of the parent class
        Person.__init__(self,name,idnumber)

#creating an object of the child class
salary = input("Enter your salary: ")
post = input("Enter your post: ")
employee1 = Employees(name, idnumber, salary, post)

print(employee1.name)
print(employee1.idnumber)
print(employee1.salary)
print(employee1.post)

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Huzaifa", "Asghar", "\nCompleted Class 10th in 2026")
x.printname()
print(x.graduationyear)


from abc import ABC, abstractmethod
#creat an abstract class
# create a base class

class Animal(ABC):

    # abstract method
    # should be implemented by all sub-classes
    @abstractmethod
    def move(self):
        pass

# sub classes

class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        print("I can crawl")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("I can roar")


# Driver code

R = Human()

R.move()

K = Snake()

K.move()

R = Dog()

R.move()

K = Lion()

K.move()


class cat :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Persian cat. My name is {self.name} and I am {self.age} years old.")  

    def make_sound(self):
        print("Meow!!!")

class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"\n I am a Husky.My name is {self.name}and I am {self.age} years old.")  

    def make_sound(self):
        print("Bark!!!")

Persian = cat("Tayo", 2)
Husky = dog("Tommy", 3)

for animal in (Persian, Husky):
    animal.info()
    animal.make_sound()

class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self,price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

#using setter function
c.setMaxPrice(2000)
c.sell()



import math

class Pentagon:
    def __init__(self, side):
        self.side = side

    def area(self):
        return (5 * self.side ** 2) / (4 * math.tan(math.pi / 5))

    def display(self):
        print(f"Pentagon area: {self.area()}")


class Hexagon:
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3 * math.sqrt(3) * self.side ** 2) / 2

    def display(self):
        print(f"Hexagon area: {self.area()}")


class Heptagon:
    def __init__(self, side):
        self.side = side

    def area(self):
        return (7 * self.side ** 2) / (4 * math.tan(math.pi / 7))

    def display(self):
        print(f"Heptagon area: {self.area()}")


# INPUT
n = int(input("Enter number of sides (5, 6, 7): "))
side = float(input("Enter side length: "))

# LOGIC
if n == 5:
    obj = Pentagon(side)
elif n == 6:
    obj = Hexagon(side)
elif n == 7:
    obj = Heptagon(side)
else:
    print("Unsupported polygon")
    exit()

obj.display()