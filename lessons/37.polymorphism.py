# ================================================
# 🧠 Polymorphism in Python - FULL DETAILED DEMO
# ================================================

# Polymorphism literally means "many forms".
# In programming, it allows objects of different classes to be treated as objects of a common superclass.
# You can call the same method (e.g., area(), draw(), add()) on different types of objects,
# and they will behave differently depending on the actual class of the object.

# ✅ Why is this powerful?
# You can write **generic**, reusable code that works across different object types
# without knowing their specific class in advance.

# --------------------------------------------------------------------
# 📦 Base class - acts like a blueprint for all shape types
class Shape:
    def __init__(self, color, dimension):
        self.color = color           # All shapes will have a color (string)
        self.dimension = dimension   # All shapes will have a dimension (e.g. "2D", "3D")

    def area(self):
        # This is a placeholder method meant to be overridden in subclasses.
        print("Generic area - should be overridden by child classes")


# ------------------------------------------------------
# 🟠 Circle class inherits from Shape and overrides area()
class Circle(Shape):
    def __init__(self, color, dimension, radius):
        super().__init__(color, dimension)  # Call the parent class (Shape) constructor
        self.radius = radius                # Circle-specific attribute

    def area(self):
        # Overridden area method specific to Circle
        print(f"🔵 Area of the circle is: {3.14 * (self.radius ** 2)}")


# ------------------------------------------------------
# 🔺 Triangle class inherits from Shape and overrides area()
class Triangle(Shape):
    def __init__(self, color, dimension, side):
        super().__init__(color, dimension)
        self.side = side

    def area(self):
        # Overridden area method specific to Triangle
        print(f"🔺 Area of the triangle is: {0.5 * self.side * self.side}")


# ----------------------------------------------------------
# ✅ Real-world polymorphism: same method name, different behavior

# Creating a list of different shapes
shape_list = [
    Circle("Red", "2D", 5),       # A Circle object
    Triangle("Yellow", "2D", 12)  # A Triangle object
]
#creating list is not necessary to achieve polymorphism its just another way of creating objects without naming each one of them and can be accessed via list indexing or a for loop 

# This prints something like: <__main__.Circle object at 0x000002...>
# Because you're printing an object directly, and there's no __str__() method.
print(shape_list[0])

# Accessing attributes directly
print(shape_list[0].color)  # Red

# The power of polymorphism:
# We can loop through different objects and call the same method: area()
for shape in shape_list:
    # Python dynamically figures out which version of area() to call.
    # This is called **dynamic dispatch** or **runtime polymorphism**.
    shape.area()

# =====================================================
# 🔥 Duck Typing in Python
# =====================================================

# Duck Typing is based on the philosophy:
# "If it walks like a duck and quacks like a duck, it's a duck."
# In Python, we care more about behavior (methods/attributes) than actual types.

# Below classes are completely unrelated — no inheritance at all.

class Artist:
    def draw(self):
        print("🎨 Artist draws a painting")

class Architect:
    def draw(self):
        print("📐 Architect draws a blueprint")

class Developer:
    def draw(self):
        print("🧑‍💻 Developer draws a flowchart")

# Now imagine a function that doesn't care "who" is drawing.
# It just expects that the object passed to it has a draw() method.
def start_drawing(person):
    # As long as the object passed in has a .draw() method, it works
    person.draw()

# Each of these is a different class, yet all support the same interface: draw()
start_drawing(Artist())     # 🎨 Artist draws a painting
start_drawing(Architect())  # 📐 Architect draws a blueprint
start_drawing(Developer())  # 🧑‍💻 Developer draws a flowchart

# No base class, no inheritance — just behavior-based polymorphism (Duck Typing)

# =====================================================
# ➕ Operator Overloading in Python
# =====================================================

# Operator Overloading lets you redefine how operators like +, *, == work for custom objects

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __add__ is the dunder method (magic method) for +
    def __add__(self, other):#self and other are not keywords you can use s and r or anything other
        return Vector(self.x + other.x, self.y + other.y)

    # String representation to print vectors nicely
    def __str__(self):
        return f"📍 Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)

# This internally calls v1.__add__(v2)
v3 = v1 + v2
print(v3)  # 📍 Vector(7, 10)

# Without operator overloading, the + operator would throw a TypeError


#python does not support method overloading as in c++ or java (same method name different number of parameters), it just selects the method that is last declared basically

class Demo:
    def greet(self):
        print("Hello!")

    def greet(self, name):
        print(f"Hello, {name}!")

# Try calling the no-argument greet
d = Demo()
d.greet()

# ❗Output: Hello, <name>!
# The first greet() is overwritten by the second one.
# So d.greet() will throw a TypeError: missing 1 required positional argument


#although it can be simulated by *args and **kwargs

# ========================================================
# 🧠 METHOD OVERLOADING in PYTHON (Simulated)
# ========================================================

# Traditional method overloading (like in Java/C++) doesn't work in Python
# because Python does not support multiple methods with the same name
# but different signatures.

# But we can simulate method overloading using:
# 1. Default arguments
# 2. *args and **kwargs (arbitrary positional and keyword arguments)

class Calculator:
    
    # This method behaves differently based on number of arguments
    def add(self, *args):
        # *args allows us to pass a variable number of arguments
        # Internally, args is treated as a tuple of all passed values

        if len(args) == 0:
            print("⚠️ No values to add.")
        elif len(args) == 1:
            print(f"🧮 Only one value: {args[0]}")
        else:
            total = sum(args)
            print(f"🧮 Sum of all values: {total}")

# Creating object
calc = Calculator()

# Now trying different 'overloads'
calc.add()             # ⚠️ No values to add.
calc.add(5)            # 🧮 Only one value: 5
calc.add(5, 10)        # 🧮 Sum of all values: 15
calc.add(1, 2, 3, 4)   # 🧮 Sum of all values: 10


# ===============================
# ✅ Summary
# ===============================

# Polymorphism = "many forms" → same interface behaves differently

# Types of Polymorphism:
# ----------------------
# 1. Duck Typing        → Based on behavior, not inheritance
# 2. Method Overriding  → Subclass provides its own implementation
# 3. Operator Overloading → Redefine how operators behave for custom types

# Benefits:
# ---------
# - Promotes flexible, reusable, and scalable code
# - Makes your design clean and modular
# - Enables writing generic functions and frameworks

