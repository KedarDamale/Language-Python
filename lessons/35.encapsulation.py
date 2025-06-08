# ================================================
# 🎓 DEMONSTRATION OF ENCAPSULATION IN PYTHON
# ================================================

# 🧠 Encapsulation is a core concept in Object-Oriented Programming (OOP)
# It means keeping the internal state (data) of an object hidden from the outside
# and exposing only selected information and methods to interact with it.

# 💡 You bind (i.e., combine) attributes and related methods inside a class,
# and control access using access modifiers: public, protected, private.

# ================================
# 📦 Let's simulate a Student System
# ================================

class Student:

    # -----------------------------------------------
    # 🏗️ Constructor (__init__) is a special method
    # It is automatically called when an object is created.
    # -----------------------------------------------
    def __init__(self, name, roll, percentage):
        self.name = name               # ✅ Public attribute: can be accessed and modified freely
        self._roll = roll              # ⚠️ Protected attribute: meant for internal use or subclass access only
        self.__percentage = percentage # 🔒 Private attribute: should never be accessed directly

        # 🔐 self.__percentage is private:
        # Python internally renames it to _Student__percentage (name mangling)
        # This makes it harder (but not impossible) to access from outside the class.

    # ----------------------------
    # 📘 Public method
    # ----------------------------
    def display_info(self):
        print("📄 Student Details:")
        print("👤 Name       :", self.name)          # Public access: OK
        print("🆔 Roll No.   :", self._roll)         # Protected: OK (inside class)
        print("📊 Percentage :", self.__percentage)  # Private: OK (inside class)

    # ----------------------------
    # 📥 Public Setter method
    # ----------------------------
    def set_percentage(self, new_percent):
        # You can add validations here
        if 0 <= new_percent <= 100:
            self.__percentage = new_percent
            print("✅ Percentage updated successfully.")
        else:
            print("❌ Invalid percentage. Must be 0 to 100.")

    # ----------------------------
    # 📤 Public Getter method
    # ----------------------------
    def get_percentage(self):
        return self.__percentage

# ===========================================
# 🎯 Let's understand Encapsulation in action
# ===========================================

# Create an object (instance) of Student class
s1 = Student("Kedar", 101, 92.5)

# ✅ Public attribute access: ALLOWED
print("\n🔓 Public Access:")
print("Name:", s1.name)

# ✅ You can also modify public attribute from outside
s1.name = "Kedar Damale"
print("Updated Name:", s1.name)

# ⚠️ Protected attribute access: TECHNICALLY ALLOWED but DISCOURAGED
# By convention, you should NOT access _roll outside the class
print("\n⚠️ Protected Access (should avoid):")
print("Roll Number:", s1._roll)  # Still works, but it's bad practice

# ❌ Private attribute direct access: NOT ALLOWED
print("\n🚫 Private Access (not allowed):")
# print(s1.__percentage)  # ❌ Will raise AttributeError if uncommented

# ✅ Accessing private data through getter method
print("Accessed via Getter:", s1.get_percentage())

# ✅ Updating private data using setter method
s1.set_percentage(88.8)

# ✅ Viewing updated percentage through public method
s1.display_info()

# ❗ HACK: You can still access private attribute using name mangling
print("\n🛠️ Name Mangling Bypass (not recommended):")
print("Accessing private var directly:", s1._Student__percentage)  # Works but defeats encapsulation

# ================================================
# 🧠 Creating a Subclass to demonstrate _protected
# ================================================

class Topper(Student):

    def __init__(self, name, roll, percentage, subject):
        super().__init__(name, roll, percentage)  # Reuse parent constructor
        self.subject = subject

    def display_topper_info(self):
        print("\n🏆 Topper Info:")
        print("Name:", self.name)             # ✅ Public access from parent
        print("Subject:", self.subject)
        print("Roll Number:", self._roll)      # ✅ Accessing protected from subclass
        # print(self.__percentage)            # ❌ Cannot access private directly
        print("Percentage:", self.get_percentage())  # ✅ Access via getter


# Create topper object
t1 = Topper("Kedar", 102, 98.7, "Python")

# Use subclass method to display data
t1.display_topper_info()

# ======================================
# 📌 ENCAPSULATION SUMMARY (RECAP)
# ======================================

# 🔓 Public members:
# - Accessible anywhere (inside class, subclass, or outside).
# - Syntax: self.variable

# ⚠️ Protected members:
# - Meant to be used only inside class or subclass.
# - Python allows access from outside, but it's a convention not to.
# - Syntax: self._variable

# 🔒 Private members:
# - Strictly internal to class.
# - Python uses name mangling to protect them.
# - Syntax: self.__variable
# - Internally becomes self._ClassName__variable and can be used by this directly outside class (bypassing encapsulation) but defeats whole purpose

# 📙 Benefits of Encapsulation:
# - Hides sensitive data and internal logic
# - Enforces modular and maintainable code
# - Provides controlled interfaces (getters/setters)
# - Allows validation when changing values
# - Makes debugging and understanding code easier

# ✅ Final Note:
# Python does not enforce access restrictions like C++/Java.
# But as a professional developer, you should respect conventions for maintainability.

