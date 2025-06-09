# dunder methods: Dunder methods or double underscore methods Such as __init__,__str__ __eq__,__name__ etc
# they are automatically called by many of python's built in operations
# they allow developers to define or customize the behavior of objects
# While they’re used most often inside classes, some built-in dunder methods exist in modules, functions, etc. Example: __name__, __main__, __file__ exist at module-level.
# These methods are always surrounded by double underscores: __init__, __str__, __eq__, etc.
# They allow you to define custom behavior for built-in operations (print, ==, +, etc.)
# They are NOT keywords — just predefined method names Python looks for.
#Dunder methods are how Python "talks" to your objects behind the scenes.



class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        #when object is created python calls __inint__ method automatically and by defining it we are custimizing it according to our needs such as initialization
    
    def __str__(self):
        return f"{self.title} by {self.author}"  
    
    def __eq__(self,other):#self and other and even cls are not keytword they are just names we can use s and o instead
        return True if self.title == other.title and self.author == other.author else False
        #return self.title == other.title and self.author == other.author basically same

b1=Book("Harry Potter 1","JKrow")
b2=Book("Harry Potter 1","JKrow")


print(b1) #when we print the object we get the memory address like this <__main__.Book object at 0x0000022A3BD94510> we can chage that using __str__
#after defining __str__ now we get Harry Potter 1 by JKrow

print(b1 == b2)#False as they are differnt objects even thry are the same book 
#we can chage that to customize the behaviour of __eq__ which is called when we use == to out needs here
#here if the title and the author is same then the object(book) is same so we define __str__

#theer are dunder methods available for each opration such as less that __lt__ greter than __gt__ addition __add__ and much more, you will see them customizing behaviour of objects in OOP and operatotr overloading

# | Dunder Method  | Triggered By         | Purpose                                  |
# | -------------- | -------------------- | ---------------------------------------- |
# | `__init__`     | Object creation      | Initialize the object (constructor)      |
# | `__str__`      | `str()` or `print()` | Human-readable string                    |
# | `__repr__`     | `repr()` / debugging | Official representation (for developers) |
# | `__eq__`       | `==`                 | Equality comparison                      |
# | `__lt__`       | `<`                  | Less than comparison                     |
# | `__gt__`       | `>`                  | Greater than comparison                  |
# | `__add__`      | `+`                  | Addition operator overloading            |
# | `__len__`      | `len()`              | Return length                            |
# | `__getitem__`  | `obj[key]`           | Index access                             |
# | `__setitem__`  | `obj[key] = value`   | Set item by key                          |
# | `__delitem__`  | `del obj[key]`       | Delete item by key                       |
# | `__call__`     | `obj()`              | Make the object callable like a function |
# | `__contains__` | `in`                 | Membership check                         |
# | `__iter__`     | `for item in obj:`   | Make object iterable                     |


