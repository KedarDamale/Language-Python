# # OOP = Object-Oriented Programming

# Object-Oriented Programming is a programming paradigm that organizes software design around **objects**.
# Objects are real-world entities (like car, student, etc.) that have:
#   - **Attributes (data)** — represented as variables inside the object.
#   - **Behaviors (actions)** — represented as methods (functions that belong to the object).

# The main building blocks of OOP are:
#   1. **Class**: A blueprint or template for creating objects.
#   2. **Object**: An instance of a class that holds actual data and behaviors.

# ------------------------
# Example 1: Defining a simple class and creating objects
# ------------------------

class Car:
    def __init__(self, model, year, color, for_sale):
        # __init__ is the constructor — it runs automatically when an object is created.
        # 'self' refers to the current object being created.
        # The values on the right (like model, year) are parameters passed while creating the object.
        # The left ones (self.model etc.) are attributes assigned to the object.
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

# Creating an object of class Car
tesla = Car("Model 3", '2020', 'Red', True)

# When you print the object directly, it shows memory location (not user-friendly)
print(tesla)  # Output: <__main__.Car object at 0x...>

# To access object's data, use dot (.) operator:
print(tesla.model)  # Output: Model 3

# Creating another object without needing a new class:
nexon = Car("Tata Nexon", '2024', 'White', True)
print(nexon.model)  # Output: Tata Nexon

# NOTE:
# - Each object has its own separate set of attributes.
# - `self` is always the first parameter in methods and refers to the object calling the method.
# - Constructor (`__init__`) is optional, but when used, it allows setting object data during creation.

# ------------------------
# Example 2: Adding a method to a class
# ------------------------

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):  # A method — a function tied to a class.
        print(f"You drive the {self.model}")

# Creating an object and calling its method
nexon = Car("Tata Nexon", '2024', 'White', True)
nexon.drive()  # Output: You drive the Tata Nexon

# ------------------------
# Example 3: Class Variables vs Object Variables
# ------------------------

class Student:
    # Class variable — shared among all objects of this class
    institute = "FAMT"

    def __init__(self, name, age, grade):
        # Object variables — specific to each object
        self.name = name
        self.age = age
        self.grade = grade

    def describe(self):
        print(f"{self.name} goes to {self.institute}")

# Creating two different student objects
kedar = Student("Kedar Pravin Damale", 21, 8.96)
pravin = Student("Pravin", 56, 8.90)

# Both share the same class variable value
kedar.describe()  # Output: Kedar Pravin Damale goes to FAMT
pravin.describe() # Output: Pravin goes to FAMT

# Verifying class variable memory ID (same for all objects)
print(f"{kedar.institute} ID: {id(kedar.institute)}")
print(f"{pravin.institute} ID: {id(pravin.institute)}")
print(f"{Student.institute} ID: {id(Student.institute)}")

# Best practice: Access class variables using the class name to clearly differentiate from instance variables
# ClassName.variable is better than object.variable

# ------------------------
# Example 4: Using Class Variables to Track All Instances
# ------------------------

class Fruits:
    # Class variables
    num_of_fruits = 0
    fruit_list = []

    def __init__(self, name, quantity):
        self.name = name            # object variable
        self.quantity = quantity    # object variable
        Fruits.num_of_fruits += 1   # update shared class variable
        Fruits.fruit_list.append(self.name)  # add name to class-level list

# Creating multiple objects
apple = Fruits("Apple", 30)
banana = Fruits("Banana", 20)
guava = Fruits("Guava", 10)
mango = Fruits("Mango", 25)

# Shared data tracked across all objects
print(Fruits.num_of_fruits)  # Output: 4
print(Fruits.fruit_list)     # Output: ['Apple', 'Banana', 'Guava', 'Mango']

# Notes:
# - `self.name` and `self.quantity` belong to the individual object.
# - `Fruits.num_of_fruits` and `Fruits.fruit_list` are shared among all objects.
# - This is useful for logging, tracking statistics, or caching common values.
