# # An exception is an event that interrupts the normal flow of a program.
# # It is also called a runtime error.
# # Examples of exceptions include ZeroDivisionError, TypeError, ValueError, etc.
# # In Python, exceptions are handled using try, except, else, and finally keywords.

# # syntax:

# try:
#     # risky code block
# except Exception or SpecificException as variable_name:
#     # what to do if that specific exception occurs
# else:
#     # optional block: executes only if no exception is raised in try
# finally:
#     # cleanup code: always executes whether exception occurs or not (optional)

# # basic example of try-except-finally
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(f"Division of these is: {a/b}")
except Exception:
    # catching all exceptions is a bad practice as it gives no detail about what went wrong
    print("Value of the denominator can't be zero or invalid input provided.")
finally:
    # this block runs no matter what
    print("Program ended!")

# # problem with the above is that since we are catching all Exception types,
# # we can't know specifically what went wrong (ValueError? ZeroDivisionError? etc.)

# # better way is to catch specific exceptions one by one
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(f"Division of these is: {a/b}")
except ValueError:
    # occurs if input is not a number
    print("ValueError: Non-integer input provided.")
except ZeroDivisionError:
    # occurs when denominator is 0
    print("ZeroDivisionError: Cannot divide by zero.")
except TypeError:
    # occurs if operation is done on incompatible types
    print("TypeError: Incompatible types.")
except Exception:
    # any other exception not caught above
    print("Another unknown exception occurred.")
finally:
    print("Program ended!")

# # The order of except blocks matters.
# # First one that matches will be executed, others will be skipped.
# # Think of it like if-elif-else structure.

# # We can use 'as' keyword to extract and print exception message
# # But below example is wrong because 'Exception' is a class, not the error object

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(f"Division of these is: {a/b}")
except Exception:
    # This will not show the actual error message, just the Exception class name
    print(f"Value error: {Exception}")  # Value error: <class 'Exception'>
finally:
    print()

# # Correct way to use 'as' is shown below
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(f"Division of these is: {a/b}")
except Exception as e:
    # e stores the actual exception object with message
    print(f"Value error: {e}")  # e.g., division by zero or invalid literal for int()
finally:
    print()

# # Summary:
# # try      ➜ block of code that may raise exception
# # except   ➜ handles specific or generic exceptions
# # as e     ➜ lets us access the exception message
# # finally  ➜ executes always, good for cleanup
# # else     ➜ executes if try block does NOT raise an exception (not used above)







# # `raise` in Python is used to intentionally trigger (raise) an exception
# # It is useful when you want to enforce certain conditions or rules in your code
# # or when a function needs to signal that an error has occurred manually

# # syntax:
# raise ExceptionType("custom error message")

# # You can raise both built-in exceptions (like ValueError, TypeError, etc.)
# # or define and raise your own custom exceptions

# example 1: manually raising built-in exceptions

try:
    age = int(input("Enter your age: "))
    if age < 0:
        # if age is negative, raise a ValueError manually
        raise ValueError("Age cannot be negative")  # this will jump to the except block
    print(f"Your age is: {age}")
except ValueError as e:
    # catch the manually raised ValueError
    print(f"Exception caught: {e}")
finally:
    print("Program completed.\n")


# example 2: raising TypeError intentionally if wrong type is passed

try:
    def greet(name):
        if not isinstance(name, str): #isinstance method is used to check if the varaible if of given type or not returns true or false
            # if name is not a string, raise TypeError
            raise TypeError("Name must be a string")
        print(f"Hello, {name}!")

    greet("Kedar")     # valid
    greet(123)         # will raise TypeError
except TypeError as e:
    print(f"Exception caught: {e}")
finally:
    print("Function execution ended.\n")


# example 3: using raise with custom exception class

# # we can define our own exception class by inheriting from Exception

class MyCustomError(Exception):
    # custom exception for demonstration
    pass

try:
    score = int(input("Enter score: "))
    if score > 100:
        # raise a custom exception if score is unrealistic
        raise MyCustomError("Score cannot exceed 100")
    print(f"Score is valid: {score}")
except MyCustomError as e:
    print(f"Custom Exception caught: {e}")
finally:
    print("Custom exception check completed.\n")


# # Summary:
# - `raise` is used to throw an exception manually
# - It interrupts normal flow and jumps to nearest matching except block
# - Can be used with built-in exceptions or custom ones
# - Use it for input validation, contract enforcement, debugging, etc.
