# ==========================================================
# ✅ PYTHON MODULES — EVERYTHING IN ONE PROGRAM (WITH NOTES)
# ==========================================================

# 🔹 A **module** is simply a `.py` file containing **functions, classes, or variables**.
# 🔹 It lets us organize code in separate files and reuse it in other programs.
# 🔹 It promotes **modularity**, **readability**, **reusability**.

# ================================
# ✅ BUILT-IN MODULES EXAMPLE
# ================================

import math  # math is a built-in standard module

print(math.sqrt(16))       # 4.0
print(math.factorial(5))   # 120
print(math.pi)             # 3.14159...
print(math.ceil(4.3))      # 5

# ================================
# ✅ DIFFERENT WAYS TO IMPORT
# ================================

# 1. import module
import random
print(random.randint(1, 10))

# 2. from module import function
from math import pow
print(pow(2, 3))  # 8.0

# 3. from module import * (not recommended, pollutes namespace A namespace is a container or mapping that associates names (identifiers) (like variables, functions, classes, etc.) 
# with the objects they refer to in memory.
# Think of a namespace like a dictionary:
# { name (str) ➝ object (value in memory) })


from math import *
print(floor(3.7))  # 3

# 4. import with alias
import statistics as stats
print(stats.mean([2, 4, 6]))  # 4

# ================================
# ✅ dir() — list attributes of a module
# ================================
print(dir(math))  # All functions & constants in math module

# ================================
# ✅ sys.path — how Python finds modules
# ================================

import sys
print(sys.path)

# Python looks for modules in these directories:
#   - Current directory
#   - PYTHONPATH (env variable)
#   - Standard library paths
#   - Site-packages (for pip-installed modules)

# ================================
# ✅ CUSTOM MODULES
# ================================

# 🔧 Suppose you have a file named myutils.py with:
'''
# File: myutils.py
def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"
'''

# You can import and use it like:
# import myutils
# print(myutils.add(2, 3))
# print(myutils.greet("Kedar"))

# Or:
# from myutils import add
# print(add(5, 6))

# ✅ Make sure myutils.py is in the same directory or in sys.path

# ================================
# ✅ __name__ == "__main__"
# ================================

# 🔹 Every Python file has a built-in variable __name__
# 🔹 When the file is run directly, __name__ == "__main__"
# 🔹 When imported, __name__ == module name
# 🔹 So we can protect certain code from running when imported

'''
# File: myutils.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Running as main")
    print(add(5, 5))
'''

# Now when you do:
#   python myutils.py → runs main block
#   import myutils → main block is NOT executed

# ================================
# ✅ pip and THIRD-PARTY MODULES
# ================================

# 🔹 You can install modules using pip
# pip install module_name

# Example:
# pip install numpy

import numpy as np #as keyword is used just to name the module so that we can write np.array instead of numpy.array
arr = np.array([1, 2, 3])
print(arr * 2)  # [2 4 6]

# You can also check installed packages:
# pip list

# You can uninstall packages:
# pip uninstall module_name

# ================================
# ✅ PACKAGE vs MODULE
# ================================

# 🔹 Module: A single .py file
# 🔹 Package: A folder with an __init__.py file (can contain multiple modules)

'''
myproject/
│
├── main.py
└── utils/
    ├── __init__.py
    ├── mathops.py
    └── stringops.py
'''

# You can do:
# from utils.mathops import add

# ================================
# ✅ Summary
# ================================

'''
🧩 A Python module is any .py file containing code.

📚 You can:
   • Import built-in modules like `math`, `os`, `random`
   • Create your own `.py` modules
   • Install external modules with `pip`

🛠️ Use `__name__ == "__main__"` to write test code that won't run on import.

📂 Packages are folders of modules; modules are individual Python files.

🔍 Python finds modules using `sys.path`
'''

# ✅ End of Program
