# ================================================================
# ✅ PYTHON SCOPES, LEGB RULE, GLOBAL/NONLOCAL, CLOSURES — IN ONE
# ================================================================

# 🔸 Built-in Scope — These are names pre-defined in Python, like `len`, `max`, `abs`, etc.
print("🔹 Built-in function abs(-7):", abs(-7))  # 7

# 🔸 Global Scope — Variables defined at the top-level of the script or module
x = "global_x"  # Global variable

def global_scope_demo():
    print("🔹 Accessing global 'x' inside function:", x)

global_scope_demo()


# 🔸 Local Scope — Variables defined inside a function only exist within that function
def local_scope_demo():
    y = "local_y"  # Local variable to this function
    print("🔹 Inside local_scope_demo, y =", y)

local_scope_demo()
# print(y)  # ❌ Error: y is not defined in global scope


# 🔸 Enclosing Scope — When one function is nested inside another, the outer function's local variables are in enclosing scope
def outer():
    z = "enclosing_z"  # Enclosing scope for inner()
    
    def inner():
        print("🔹 inner() sees enclosing z:", z)  # z is found in enclosing scope

    inner()

outer()


# ================================================================
# ✅ LEGB RULE — Scope Resolution Order
# ================================================================

# Python searches for variable in this order:
# L — Local
# E — Enclosing
# G — Global
# B — Built-in

a = "global_a"  # Global scope

def outer_func():
    a = "enclosing_a"  # Enclosing scope
    
    def inner_func():
        a = "local_a"  # Local scope
        print("🔹 LEGB Resolution — a =", a)  # Will print local_a

    inner_func()

outer_func()


# ================================================================
# ✅ GLOBAL KEYWORD — To modify global variable from inside a function
# ================================================================

counter = 0  # Global variable

def increment():
    global counter  # Declares we are using the global 'counter'
    counter += 1    # Modifies the global variable
    print("🔹 counter inside increment() =", counter)

increment()
print("🔹 counter in global scope =", counter)


# ================================================================
# ✅ NONLOCAL KEYWORD — To modify enclosing variable in nested functions
# ================================================================

def outer_nonlocal():
    msg = "Hello"

    def inner_nonlocal():
        nonlocal msg  # Refers to 'msg' from outer_nonlocal()
        msg = "Hi"

    inner_nonlocal()
    print("🔹 msg after modification by inner_nonlocal():", msg)

outer_nonlocal()


# ================================================================
# ✅ CLOSURES — Functions capturing variables from enclosing scope
# ================================================================

def multiplier(factor):
    # 'factor' is part of enclosing scope for returned function
    def multiply_by(n):
        return n * factor  # Uses enclosing variable

    return multiply_by  # Returns a closure

times2 = multiplier(2)  # Creates a closure where factor=2
times3 = multiplier(3)  # Creates another closure where factor=3

print("🔹 Closure times2(5):", times2(5))  # 10
print("🔹 Closure times3(5):", times3(5))  # 15

# Closure retains the environment where it was created (factor=2 or 3)


# ================================================================
# ✅ SCOPE ISOLATION — Each function has its own variable namespace
# ================================================================

def func1():
    val = 10
    print("🔹 func1() val =", val)

def func2():
    val = 20
    print("🔹 func2() val =", val)

func1()
func2()
# The same variable name `val` in both functions does not conflict


# ================================================================
# ✅ SUMMARY
# ================================================================

'''
🔸 Scope defines where a variable can be accessed from.

🔸 LEGB Rule:
    • Local — Inside current function
    • Enclosing — Inside any outer functions
    • Global — Top-level script/module
    • Built-in — Python-provided names

🔸 `global` — Declares a variable to be from the global scope
🔸 `nonlocal` — Declares a variable to be from the enclosing function

🔸 Closures — Inner functions that capture variables from outer scopes

🔸 Each function has its own namespace; variables do not leak between them.
'''

# ✅ End of program
