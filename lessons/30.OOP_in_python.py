# # OOP=object oriented programming

# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects, 
# which are instances of classes. These objects encapsulate data (attributes or properties) and 
# behaviors (methods or functions) into a single unit.

#main components of OOP are objects and classes

#classes are simply a blkueprint that is used to design the structure and layout of an object 
#object is a bundle of attributes of its class , attributes maning variable and methods, objects nedd a class to get created 

#a method is a function that beloings to an objecty methods!=functions

# Syntax:
#     class class_name:
#         def __init__(self,parameters to be initialized after creating an object): #this is a 
#             self.param1=param1 #here param1 on the left in attribute of class and on the right is the one we recived
                
#         other arrtributes
#object :  object_name=Its_class(parameters for the constructor)

class Car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
        
#to create an object\

tesla=Car("Model 3",'2020','Red',True) #self doesnt need to be supplied constructor is aslo a function so all arg rules apply

print(tesla) #<__main__.Car object at 0x00000228F20B4210>

#printing object give you the memory object 
#to access something from the object we use "." which is a access operator

print(tesla.model) #Model 3

#now lets say i want to create another car named Nexon so for that we dont require to create another class we just need to create another object of the same class
Nexon=Car("tata nexon",'2024','White',True)
print(Nexon) #<__main__.Car object at 0x0000020C7F5345D0>
print(Nexon.model) #tata nexon

#classes can be created in different file and can be used to create object in different file
#classname usually created with first letter capital but its not madatory

# from filename_which_shouldbe_all_lowecase import classname
# a=classname()


class Car:
    def __init__(self,model,year,color,for_sale):
        self.model=model #sef is basically the reference to the attributes of the current object it is necessary to be included with every sttribute
        self.year=year
        self.color=color
        self.for_sale=for_sale
        
    def drive(self):
        print(f"You drive the {self.model}")
    
Nexon=Car("tata nexon",'2024','White',True)
Nexon.drive() #You drive the tata nexon

#class variables

#There are the variables that shared among all instances of a class it is defined outside the constructor it allows you to share data among all objects created from that particular class

class Student:
    institute="FAMT"
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def describe(self):
        print(f"{self.name} goes to {self.institute}")
        
        
kedar=Student("Kedar Pravin Damale",21,8.96)
kedar.describe() #Kedar Pravin Damale goes to FAMT
#here institute is a class variable that will not change from object to object but name is object varibale that is specific to that object

pravin=Student("Pravin",56,8.90)

print(f"{kedar.institute} its id is {id(kedar.institute)}")
print(f"{pravin.institute} its id is {id(pravin.institute)}")
#FAMT its id is 1816375656240
# FAMT its id is 1816375656240

# as you can see the meory location is same

# it can be acceseed by class too
print(f"{Student.institute} its id is {id(Student.institute)}") #FAMT its id is 2442398793520

# so you can access a class variable via objects and class both, its a good practice to access it via class so that we can have a clear idea that if this variable is of instace or class variable

class Fruits:
    num_of_fruits=0
    l=[]
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity
        Fruits.num_of_fruits+=1
        Fruits.l.append(self.name)
        
apple=Fruits("Apple",30)
apple=Fruits("Banana",30)
apple=Fruits("Guava",30)
apple=Fruits("Mango",30)

print(Fruits.num_of_fruits)
print(Fruits.l)

#
#['Apple', 'Banana', 'Guava', 'Mango']

#this is how data is shared among all instance
#note : self referes to that instance menas when we are using self we are basically using apple.name banna.name and so on 
#when it comes to calss varibale because they are common and share one  value and memory location they can only be accessed and modified by classname.varname