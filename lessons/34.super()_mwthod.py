# -------------------------------
# PYTHON OOP: USING super() IN DEPTH
# -------------------------------

# ✅ SUPER FUNCTION:
# - Used inside a child class to call methods from its parent class
# - Helps extend or reuse functionality from the superclass
# - Useful for constructor chaining and method overriding

# 👇 Real-world Example:
# We are modeling geometric shapes, and every shape has a color.
# Instead of repeating color logic in every class, we define it once in a base class.

# -------------------------------
# 1. BASE CLASS
# -------------------------------

class Shape:
    def __init__(self, color):
        self.color = color  # color is a common attribute for all shapes

    def describe(self):
        print(f"This shape has {self.color} color")  # general description method

# -------------------------------
# 2. CHILD CLASS Circle
# -------------------------------

class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius  # Circle-specific attribute
        # Now we want to also assign the color from Shape
        # Instead of doing self.color = color again, we use super()
        super().__init__(color)  # ✅ Calls Shape's constructor

# -------------------------------
# 3. CHILD CLASS Square
# -------------------------------

class Square(Shape):
    def __init__(self, side, color):
        self.side = side  # Square-specific attribute
        # Calling parent constructor for shared attribute
        super().__init__(color)

# -------------------------------
# 4. OBJECT CREATION
# -------------------------------

# Creating Circle object
c = Circle(3.45, "Yellow")
c.describe()  # Output: This shape has Yellow color

# Creating Square object
s = Square(5.6, "Blue")
s.describe()  # Output: This shape has Blue color

# ✅ Explanation:
# - Although we only explicitly set radius/side in child constructors,
#   the parent constructor was still called to set `color` thanks to `super()`
# - So we don’t repeat code

# -------------------------------
# 5. EXTENDING METHODS USING super()
# -------------------------------

# What if child class needs to *add* to the parent’s method rather than *replace* it?

class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        super().__init__(color)

    def describe(self):
        # Extended behavior: Describe radius first
        print(f"This Circle has a radius of {self.radius}")
        # Then call the parent method to describe color
        super().describe()  # Calls Shape.describe()

# Now test again:
c = Circle(3.45, "Yellow")
c.describe()

# Output:
# This Circle has a radius of 3.45
# This shape has Yellow color

# ✅ This is method overriding + extension
# - We're not replacing describe() completely
# - We're adding new functionality *before* calling parent logic

# -------------------------------
# 6. BEHAVIOR OF super()
# -------------------------------

# Internally:
# - super() returns a proxy object of the parent class
# - It does NOT return the parent object — it routes the call through MRO (method resolution order)
# - This helps especially in multiple inheritance scenarios (avoids redundant calls)

# MRO Check
print("MRO of Circle:", Circle.__mro__)
# Output: (<class '__main__.Circle'>, <class '__main__.Shape'>, <class 'object'>)

# -------------------------------
# FINAL NOTES:
# -------------------------------
# 🧠 super().__init__() is best for constructor reuse — avoids duplicate code
# 🧠 super().method() is best for method overriding + extension
# 🧠 Always prefer super() over hardcoding parent class names (like Shape.__init__) for flexibility and maintainability
# 🧠 Only immediate parent is called; super() doesn't jump across siblings or unrelated classes
# 🛑 Don’t forget to match the arguments expected by the parent when using super()

# -------------------------------
# END OF PROGRAM
# -------------------------------
