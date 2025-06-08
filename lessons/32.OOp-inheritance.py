# ------------------------
# Inheritance in Python
# ------------------------

# ✅ Definition:
# Inheritance allows a class (child/derived class) to **reuse** the properties and methods 
# of another class (parent/base class), promoting code **reusability** and **extensibility**.

# ✅ Syntax:
# class ChildClass(ParentClass):
#     # optional override methods or define new ones
#     pass

# Example hierarchy:
# Animal (base class)
# ├── Dog (inherits Animal)


# ------------------------
# Base class
# ------------------------

class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True  # This is an instance variable, unique to each object Note^^^

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def eat(self):
        print(f"{self.name} is eating.")


# ⚠️ Just because a variable (like isAlive) has the same value for all objects,
# it does NOT mean it is a class variable.

# Class variables are defined outside any method using ClassName.varName.
# They share memory (same `id()`) for every object.
# Instance variables (like self.isAlive) are created **inside __init__** and exist separately in each object’s memory.

# You CANNOT pass instance variables between objects — they belong to individual instances.
# But class variables CAN be shared and accessed by all.



# ------------------------
# Child class without override
# ------------------------

# If you don't define any methods or constructors, the child class automatically
# inherits everything (variables and methods) from the parent.
class Dog(Animal):
    pass

d = Dog("Phoenix")  # Inherits Animal's constructor
d.sleep()           # Output: Phoenix is sleeping. (Inherited from Animal)
d.eat()             # Output: Phoenix is eating.

# When we created Dog("Phoenix"), it internally called Animal.__init__ because
# Dog doesn’t have its own constructor defined.


# ------------------------
# Child class with new method
# ------------------------

# Child classes can add new methods.
class Dog(Animal):
    def voice(self):  # New method, not in Animal
        print(f"{self.name} barks!")

a = Dog("Bruno")
a.voice()   # Output: Bruno barks!
a.sleep()   # Output: Bruno is sleeping. (Still inherits Animal's sleep)

