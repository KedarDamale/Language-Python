# A decorator is a function that takes another function as input, wraps it, and returns a modified version of it,
# extending or modifying its behavior — without changing the original function’s source code.

# syntax:
#     @add_sprinkles
#     get_ice_cream(""vanilla") #some people just want icecream this function is for them and if some want sprinkles then we are using the 
                               #decorator function add_sprinkles to extend get_ice_cream()




def get_ice_cream():
    print("Here is you icecream")
    
get_ice_cream()#Here is you icecream

#formula to create a decorator:

# #def dec_function(normal_function):
#     def wrapper():
#         code Block
#         normal_function()
#     return wrapper




def add_sprinkles(function):
    def wrapper():#we need wrapper function (wrapper is just a name) to stop code from direclty execuiting as the function will execute without a function call
        print("Added sprinkles and" ,end=" ")
        function()#here the Here is you icecream is printed basically
    return wrapper


@add_sprinkles
def get_ice_cream():
    print("Here is you icecream")
    
get_ice_cream()#Added sprinkles and Here is you icecream

    
def add_cream(function):
    def wrapper():
        print("Added cream ",end="")
        function()
    return wrapper

# we can as many decorators as we want
@add_cream
@add_sprinkles
def get_ice_cream():
    print("Here is you icecream")
    
get_ice_cream()#Added cream Added sprinkles and Here is you icecream


#Things change a little when we need to accept arguments in base function

def ice_cream(flavor):
    print(f"Here is you {flavor} ice-cream!")
    
ice_cream("Pista")#Here is you Pista ice-cream!

def sprinkles(function):
    def wrapper(*args,**kwargs):
        print("Added sprinkles and ",end="")
        function(*args,**kwargs)
    return wrapper

@sprinkles
def ice_cream(flavor):
    print(f"Here is you {flavor} ice-cream!")
    
ice_cream("pista") #Added sprinkles and Here is you pista ice-cream!

# ==========================
# 🧠 INTERNAL WORKING
# ==========================
# A decorator is just a "higher-order function":
# - Takes a function as input
# - Returns another function
# This makes decorators a form of FUNCTION WRAPPING or FUNCTION MODIFICATION

# Closures are key: The wrapper "remembers" the original function passed to the decorator.
