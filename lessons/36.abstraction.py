# ========================================================
# 🔐 ABSTRACTION IN PYTHON — Full Explanation in 1 Program
# ========================================================

# ======================
# 🧠 What is Abstraction?
# ======================

# ➤ Abstraction means hiding the **internal implementation details** and exposing **only essential features**.
# ➤ In OOP, abstraction lets you define a blueprint (interface) that forces subclasses to implement required methods.
# ➤ It answers: "What should be done?" — not "How is it done?"

# ➤ Think of abstraction as designing **skeletons** or **templates** for classes.

# ➤ Example Analogy:
#    - You use a phone to call, text, take photos.
#    - You don't know how the circuits and hardware actually work.
#    - The complex logic is hidden from you — that is **abstraction** in action!

# ========================================================
# 🔧 Python Abstraction is done using the abc module (abstract base class)
# ========================================================

# ✅ We import ABC and abstractmethod from Python’s abc (Abstract Base Class) module.
from abc import ABC, abstractmethod

# ====================================================
# 🚘 Step 1: Define an Abstract Class (Blueprint Class)
# ====================================================
class Vehicle(ABC):
    """
    Abstract Base Class — acts like a blueprint.
    You cannot create an object of this class directly.
    It forces all subclasses to implement the abstract methods.
    """

    # ------------------------------------------
    # 🛑 Abstract Method (must be overridden)
    # ------------------------------------------
    @abstractmethod
    def start_engine(self):
        """
        Abstract method — no implementation here.
        Must be implemented in the child class.
        """
        pass

    @abstractmethod
    def stop_engine(self):
        """
        Another abstract method.
        """
        pass

    # ------------------------------------------
    # ✅ Concrete Method (optional to override)
    # ------------------------------------------
    def fuel_type(self):
        """
        A normal method with implementation.
        Can be optionally overridden in subclass.
        """
        print("⛽ Fuel type: Generic (Petrol/Diesel/Electric)")

# ========================================================
# 🚗 Step 2: Create Concrete Subclasses from the Abstract Base
# ========================================================

class Car(Vehicle):
    """
    Car is a concrete class that inherits from abstract Vehicle.
    Since Vehicle has abstract methods, Car must implement all of them.
    """

    def start_engine(self):
        print("🚗 Car engine started with a key ignition or push button.")

    def stop_engine(self):
        print("🛑 Car engine stopped.")

    def fuel_type(self):
        print("⛽ Car runs on petrol or diesel.")

class ElectricScooter(Vehicle):
    """
    Another subclass of Vehicle. Demonstrates different implementation.
    """

    def start_engine(self):
        print("⚡ Scooter turned on with electric switch.")

    def stop_engine(self):
        print("🛑 Scooter turned off and power cut.")

    def fuel_type(self):
        print("🔋 Scooter runs on battery power.")

# ============================================================
# ❌ Trying to instantiate an abstract class (will raise error)
# ============================================================

# v = Vehicle()  # ❌ Not allowed: TypeError — can't instantiate abstract class with abstract methods

# ====================================================
# ✅ Instantiate Concrete Subclasses and Use Them
# ====================================================

print("\n🔧 Working with Car Object")
car = Car()
car.start_engine()        # Uses Car's implementation
car.fuel_type()           # Overridden method
car.stop_engine()

print("\n🔧 Working with Electric Scooter Object")
scooter = ElectricScooter()
scooter.start_engine()    # Uses Scooter's implementation
scooter.fuel_type()       # Overridden method
scooter.stop_engine()

# ===================================================
# 🧠 Summary of Key Abstraction Concepts in Python
# ===================================================

# ✅ Abstract Class:
# - A class that cannot be instantiated.
# - Contains one or more abstract methods.
# - Defined by inheriting from ABC.

# ✅ Abstract Method:
# - Defined using @abstractmethod decorator.
# - Must be overridden in every concrete subclass.
# - Cannot have any logic in the base class.

# ✅ Concrete Method in Abstract Class:
# - You *can* define normal methods in abstract class.
# - These can be inherited or optionally overridden.

# ✅ Why Use Abstraction?
# - Enforces consistency in subclass implementations.
# - Reduces code duplication.
# - Hides complex logic from the user.
# - Allows switching implementations easily (e.g., Car → Truck).

# ✅ Real-world use:
# - Payment systems: Abstract class `Payment`, subclasses `CardPayment`, `UPIPayment`, etc.
# - UI Elements: Abstract class `Shape`, subclasses `Circle`, `Square`, etc.
# - Hardware Drivers: Abstract `PrinterDriver`, actual implementations per printer model.

# ✅ Interview Ready One-liner:
# "Abstraction in Python is achieved using the `abc` module by hiding implementation and forcing standard interfaces in child classes."

