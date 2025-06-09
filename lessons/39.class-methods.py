# ======================================================
# 🧠 CLASS METHODS in Python — DEEPLY EXPLAINED
# ======================================================

# A class method is a method that's bound to the class and not the object (instance).
# It takes `cls` as the first argument instead of `self`.
# You use the @classmethod decorator to define a class method.

class Student:
    # =========================
    # 🎯 Class Variable
    # This variable is shared among ALL instances of the class
    # It keeps track of the total number of students
    count = 0

    def __init__(self, name, gpa):
        # These are instance variables — unique for each object
        self.name = name
        self.gpa = gpa

        # Every time a new student object is created, increment the class variable
        Student.count += 1

    # =========================
    # 📦 Instance Method
    # This operates on instance-level data and takes `self` as the first parameter
    def get_info(self):
        return f"👤 Name: {self.name}\n📊 GPA: {self.gpa}"

    # =========================
    # 🏫 Class Method
    # Operates at the class level, not instance level
    # Use @classmethod decorator and `cls` as the first parameter
    @classmethod
    def get_student_count(cls):
        # Here, cls refers to the class itself: Student
        return f"📚 Total number of students: {cls.count}"


# ===============================================
# 🧪 Let's test everything we've written

# Class method can be called even before any object is created
print(Student.get_student_count())  # Output: 0 students

# Create two student objects (instances)
s1 = Student("Kedar", 8.98)
s2 = Student("Pravin", 8.97)

# Even though this works:
print(s2.get_student_count())  # 📚 Total number of students: 2
# It is NOT recommended to call class methods via an instance.
# Instead, call it directly using the class name (below).

# Correct and recommended way to call a class method:
print(Student.get_student_count())  # 📚 Total number of students: 2

# Show student info using instance method
print(s1.get_info())
# 👤 Name: Kedar
# 📊 GPA: 8.98


# 📌 Quick Comparison: instance vs class vs static methods

# | Type            | First Param | Access Instance? | Access Class? | Use Case                            |
# | --------------- | ----------- | ---------------- | ------------- | ----------------------------------- |
# | Instance Method | `self`      | ✅ Yes            | ✅ Yes         | Access/modify object and class data|
# | Class Method    | `cls`       | ❌ No             | ✅ Yes         | Access/modify class-level data     |
# | Static Method   | ❌ None      | ❌ No             | ❌ No          | Utility functions (logic only)    
