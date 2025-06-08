# -------------------------------
# PYTHON INHERITANCE IN DEPTH
# MULTIPLE + MULTILEVEL
# -------------------------------

# -------------------------------
# MULTIPLE INHERITANCE
# -------------------------------

# First Parent Class (Base 1)
class Prey:
    def getsHunted(self):
        # Method to describe prey behavior
        print("This animal gets hunted!")

# Second Parent Class (Base 2)
class Predator:
    def hunts(self):
        # Method to describe predator behavior
        print("This animal hunts!")

# Child Class inheriting from both Prey and Predator
class Fish(Prey, Predator):
    pass  # We don't define any new methods, but it inherits all from both parents

# Creating object of Fish
f = Fish()

# Accessing methods from both parent classes
f.getsHunted()  # Output: This animal gets hunted! (from Prey)
f.hunts()       # Output: This animal hunts (from Predator)

# ✅ So, Fish is both a Prey and a Predator — multiple inheritance works
# Internally: Python uses MRO (Method Resolution Order) to resolve conflicts (left to right search)

# Note: if both Prey and Predator had a method with the same name (e.g. def info()), 
# then the method from the first parent (Prey) would be used, due to MRO

# You can check MRO using:
print("MRO of Fish:", Fish.__mro__)
# Output: (<class '__main__.Fish'>, <class '__main__.Prey'>, <class '__main__.Predator'>, <class 'object'>)


# -------------------------------
# MULTILEVEL INHERITANCE
# -------------------------------

# Top-most Base class
class Animal:
    def print_name(self):
        print("name")

# Intermediate class inheriting from Animal
class Predator(Animal):
    pass  # Inherits print_name() from Animal

# Leaf/Bottom class inheriting from Predator, which in turn inherits from Animal
class Fish(Predator):
    pass  # Indirectly inherits from Animal as well

# Object of Predator
p = Predator()
p.print_name()  # Output: name (from Animal)

# Object of Fish (grandchild class)
f = Fish()
f.print_name()  # Output: name (also from Animal, via Predator)

# ✅ So, Fish inherits methods from Predator → which inherits from Animal
# This is multilevel inheritance (Animal → Predator → Fish)

# -------------------------------
# EXPLANATION + EXTRA KNOWLEDGE
# -------------------------------

# 🧠 1. Memory-wise:
# - All objects (like `f`) are instances of the most-derived class (Fish)
# - But their __class__.__mro__ defines how method resolution happens up the chain

# 🧠 2. Top-down flow only:
# - You can access parent/grandparent methods from a child (like f.print_name())
# - BUT parents (like Animal or Predator) have no knowledge of their children (they can't access Fish-specific methods)

# 🛠️ 3. If method exists in multiple ancestors (like in multiple inheritance), Python uses:
# - C3 Linearization (left-to-right depth-first search without duplication)
# - You can see it in __mro__

# ⚠️ 4. Diamond Problem (advanced): Not relevant yet, but multiple inheritance can cause method resolution ambiguity.
# - Python handles this cleanly using MRO, unlike C++ which needs virtual inheritance

# ✅ 5. All classes ultimately inherit from `object` class in Python (this makes them "new-style" classes since Python 3)

# 🧼 6. Best Practice:
# - Always use consistent naming and class hierarchy
# - Keep the inheritance tree shallow unless absolutely needed
# - Prefer composition over inheritance when behavior varies too much

# -------------------------------
# END OF PROGRAM
# -------------------------------
