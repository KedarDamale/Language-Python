# ===========================================================
# 🔍 STATIC METHODS vs INSTANCE METHODS in Python (OOP)
# ===========================================================

# 💡 Instance methods:
# - Are the most common type of methods in classes.
# - Take `self` as their first argument (which refers to the object calling the method).
# - Can access and modify the object’s attributes.

# 💡 Static methods:
# - Defined using the `@staticmethod` decorator.
# - Do NOT take `self` or `cls` as the first argument.
# - Do NOT have access to instance (`self`) or class (`cls`) data.
# - Behave like normal functions that live inside a class's namespace.
# - Often used for utility/helper functions related to the class's concept.

class Employee:
    # ----------------------------------------------------
    # 🔹 Constructor (special method)
    # ----------------------------------------------------
    def __init__(self, name, position):
        # These are instance variables — specific to each object
        self.name = name
        self.position = position

    # ----------------------------------------------------
    # 🔹 Instance Method
    # ----------------------------------------------------
    def get_info(self):
        # Can access instance attributes like self.name and self.position
        return f"{self.name} works as a {self.position}"

    # ----------------------------------------------------
    # 🔹 Static Method
    # ----------------------------------------------------
    @staticmethod
    def is_valid_position(position):
        """
        This method checks if a given job title is valid.
        It doesn’t rely on instance (self) or class (cls) data.
        Therefore, it is marked as a static method.
        """
        valid_positions = ["CEO", "CTO", "CMO", "MD", "Janitor"]
        
        # Return "True" if the given position is valid, else a message.
        return "True" if position in valid_positions else "❌ Please enter a valid position"

# ------------------------------------------------------------
# ✅ USING STATIC METHOD WITHOUT CREATING AN OBJECT
# ------------------------------------------------------------

# This is the correct and recommended way to use static methods —
# directly through the class name.
print(Employee.is_valid_position("CEO"))  # ✅ Output: True
print(Employee.is_valid_position("dg"))   # ❌ Output: Please enter a valid position


# ------------------------------------------------------------
# 🧍 CREATING AN INSTANCE / OBJECT
# ------------------------------------------------------------

e1 = Employee("Kedar", "CEO")

# ------------------------------------------------------------
# ✅ USING INSTANCE METHOD (bound to object)
# ------------------------------------------------------------
print(e1.get_info())  # Output: Kedar works as a CEO

# ------------------------------------------------------------
# ⚠️ USING STATIC METHOD FROM INSTANCE (NOT RECOMMENDED)
# ------------------------------------------------------------

# Though Python allows it, using a static method via an object is confusing.
# It makes it seem like the method depends on the object (it does NOT).
# Still, this will work:
print(e1.is_valid_position("CEO"))  # ✅ Output: True

# ➕ Best practice: Always call static methods via ClassName.method()

