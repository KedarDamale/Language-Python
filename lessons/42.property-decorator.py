# ================================================================
# 🚪 Property Decorators in Python — Full Program & Explanation
# ================================================================

# 🧱 Imagine we want a class Rectangle with `width` and `height` that:
# 1. Returns values in centimeters when accessed
# 2. Allows setting values with input validation
# 3. Prevents invalid dimensions
# 4. Allows deleting width/height with side-effects
# We'll use property decorators to do all this in a clean way.

class Rectangle:
    def __init__(self, width, height):
        # 🟡 Protected attributes (by convention, not enforced)
        # _width and _height are intended for internal use within the class
        self._width = width
        self._height = height

    # ===============================
    # 📖 GETTER for width using @property
    # ===============================
    @property
    def width(self):
        # This method acts like an attribute when accessed: r.width
        return f"{self._width:.2f} cm"

    # ===============================
    # ✏️ SETTER for width using @width.setter
    # ===============================
    @width.setter
    def width(self, value):
        # Logic to validate before assigning
        if value <= 0:
            raise ValueError("Width must be a positive number.")
        self._width = value

    # ===============================
    # ❌ DELETER for width using @width.deleter
    # ===============================
    @width.deleter
    def width(self):
        print("⚠️ Width deleted!")
        self._width = None  # Or could use `del self._width`

    # Repeat the same for height
    @property
    def height(self):
        return f"{self._height:.2f} cm"

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive number.")
        self._height = value

    @height.deleter
    def height(self):
        print("⚠️ Height deleted!")
        self._height = None

    # ===============================
    # 🧮 Computed Property: Area
    # ===============================
    @property
    def area(self):
        # Area is computed based on current width and height
        if self._width is None or self._height is None:
            return "Dimensions are not fully set."
        return f"{self._width * self._height:.2f} sq. cm"


# ================================================================
# 🚀 Using the Rectangle class
# ================================================================

# Creating an object
r = Rectangle(4.5, 7.2)

# ✅ GETTERS — These call @property methods behind the scenes
print(f"📏 Width of rectangle: {r.width}")   # → 4.50 cm
print(f"📐 Height of rectangle: {r.height}") # → 7.20 cm
print(f"🧮 Area of rectangle: {r.area}")      # → 32.40 sq. cm

# ✅ SETTERS — These call @attr.setter methods
r.width = 10      # Sets width using custom setter logic
r.height = 15     # Same for height

# Check updated values
print(f"\n📏 New Width: {r.width}")
print(f"📐 New Height: {r.height}")
print(f"🧮 New Area: {r.area}")

# ❌ Trying to set a negative value → should raise error
try:
    r.width = -5
except ValueError as e:
    print(f"\n🚫 Error: {e}")

# 🗑️ DELETERS — These call @attr.deleter methods
del r.width
del r.height

print(f"\n📏 Width after deletion: {r.width}")    # → None cm
print(f"📐 Height after deletion: {r.height}")    # → None cm
print(f"🧮 Area after deletion: {r.area}")         # → Dimensions are not fully set.
