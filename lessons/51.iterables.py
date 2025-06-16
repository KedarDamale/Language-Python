"""
Got it, Kedar. Let’s dive deep into **Python Iterators**, covering:

* What are **iterators** and **iterables**?
* The difference: **Iterator vs Iterable**
* Key methods: `iter()`, `next()`
* Handling iteration direction (like left/right, prev/next concepts)
* How to implement custom iterators
* Common iterator-related built-ins and protocols
* Detailed example walkthroughs

---

# 1. **What is an Iterable?**

An **iterable** is any Python object capable of returning its members one at a time, allowing it to be looped over in a `for` loop or used in functions like `list()`, `sum()`, etc.

* An iterable implements the special method `__iter__()` that returns an **iterator** object.
* Examples: lists, tuples, strings, dictionaries, sets, files, generators.

```python
lst = [1, 2, 3]  # list is iterable
```

---

# 2. **What is an Iterator?**

An **iterator** is an object that represents a **stream of data**; it returns the next item when requested.

* An iterator implements the `__next__()` method (or `next()` in Python 2).
* The iterator object remembers its state during iteration.

---

# 3. **Iterator vs Iterable: Difference**

| Aspect                       | Iterable                                           | Iterator                                                |
| ---------------------------- | -------------------------------------------------- | ------------------------------------------------------- |
| Definition                   | An object you can iterate over (e.g., list, tuple) | An object that produces the next item                   |
| Protocol                     | Implements `__iter__()` method                     | Implements `__next__()` method                          |
| Usage                        | Can be used with `for` loop                        | Used by `for` loop internally, or manually via `next()` |
| Can you call `iter()` on it? | Yes (returns iterator)                             | Usually itself (iterators return themselves)            |
| Can you get multiple passes? | Yes (can create new iterators)                     | No (exhausts after one pass)                            |

---

# 4. **The `iter()` function**

`iter(obj)` returns an **iterator** from an iterable.

```python
lst = [1, 2, 3]
it = iter(lst)  # get iterator from list
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# next(it) now raises StopIteration
```

---

# 5. **The `next()` function**

`next(iterator[, default])` returns the next item from the iterator.

* Raises `StopIteration` if no more elements.
* If `default` is provided, returns it instead of raising error.

Example:

```python
it = iter([10, 20])
print(next(it))      # 10
print(next(it))      # 20
print(next(it, -1))  # -1 instead of StopIteration
```

---

# 6. **Handling `StopIteration`**

When `next()` exhausts the iterator, it raises `StopIteration` — the `for` loop handles this internally, so you rarely see it in normal code unless you manually use `next()`.

Example with manual handling:

```python
it = iter([1, 2])
while True:
    try:
        val = next(it)
        print(val)
    except StopIteration:
        break
```

---

# 7. **Prev / Left / Right: Direction in Iteration**

* **Python iterators move forward only** via `next()`.
* Python’s iterator protocol **does not support backward iteration (prev) natively**.
* To have "prev" or bidirectional iteration, you need to implement a **custom iterator**.

---

# 8. **Implementing a Bidirectional Iterator (prev and next)**

You can write a class with methods `next()` and `prev()` maintaining an index internally.

Example:

```python
class BidirectionalIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1  # starts before first element

    def next(self):
        if self.index + 1 >= len(self.data):
            raise StopIteration("Reached the end")
        self.index += 1
        return self.data[self.index]

    def prev(self):
        if self.index - 1 < 0:
            raise StopIteration("Reached the start")
        self.index -= 1
        return self.data[self.index]

# Usage
it = BidirectionalIterator([10, 20, 30])
print(it.next())  # 10
print(it.next())  # 20
print(it.prev())  # 10
```

---

# 9. **How to make an Object Iterable?**

To be iterable, an object must implement the method `__iter__()` that returns an **iterator object**. The iterator object must implement `__next__()`.

---

# 10. **Custom Iterator Example**

```python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self  # iterator returns itself

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 1
        return val

my_iter = MyIterator([1, 2, 3])

for x in my_iter:
    print(x)
```

---

# 11. **Iterable Example (Object with `__iter__`)**

```python
class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyIterator(self.data)

my_obj = MyIterable([1, 2, 3])
for val in my_obj:
    print(val)
```

---

# 12. **Summary: Iterator Protocol**

* **Iterable**: Implements `__iter__()`, returns an iterator.
* **Iterator**: Implements `__next__()` (and `__iter__()` returning self).
* `next()` calls `__next__()` internally.
* Raises `StopIteration` when exhausted.

---

# 13. **Built-in Iterators**

* Lists, tuples, dicts, sets are iterable.
* Their iterator objects are created with `iter()`.
* Generators are special iterators, they implement both `__iter__` and `__next__`.
* Files are iterable line-by-line.

---

# 14. **Useful Built-in Functions Related to Iterators**

| Function              | Purpose                                                              |
| --------------------- | -------------------------------------------------------------------- |
| `iter(obj)`           | Return an iterator from iterable `obj`                               |
| `next(it[, def])`     | Return next item from iterator or `def` if given                     |
| `enumerate(iterable)` | Return iterator that yields `(index, value)` tuples                  |
| `zip(*iterables)`     | Iterator that aggregates elements from multiple iterables            |
| `reversed(seq)`       | Returns iterator that iterates in reverse order (only for sequences) |

---

# 15. **How `for` Loop Uses Iterators Internally**

```python
for x in iterable:
    # loop body
```

is internally translated roughly to:

```python
it = iter(iterable)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    # loop body
```

---

# 16. **Iterator vs Generator**

* **Generator** is a special kind of iterator created with `yield` inside functions.
* Generator automatically implements `__iter__()` and `__next__()`.
* Useful for lazy evaluation and large data streams.

---

# **Summary Table**

| Concept       | Implements                    | Returns            | Notes                         |
| ------------- | ----------------------------- | ------------------ | ----------------------------- |
| Iterable      | `__iter__()`                  | Iterator object    | Can be looped over            |
| Iterator      | `__next__()`, `__iter__()`    | Next element       | Keeps iteration state         |
| `iter()` func | Converts iterable to iterator | Iterator           |                               |
| `next()` func | Calls `__next__()`            | Next element       | Raises `StopIteration` on end |
| Bidirectional | Custom class needed           | `next()`, `prev()` | Not built-in in Python        |

---

If you want, I can also provide:

* Code samples implementing **custom iterators** with state.
* Examples using `enumerate`, `zip`, and `reversed` (iterator utilities).
* Explain **generator functions** and how they relate to iterators.

Do you want me to do that next?

"""


"""
Absolutely, Kedar. Let's get into **Generators** — what they are, how they work, their differences from iterators, how to write them, advanced uses, and why they are important in Python.

---

# 1. **What is a Generator?**

A **generator** is a special type of **iterator** that **yields** values one at a time, **lazily**, **on demand**, instead of computing and storing all values at once.

* Generators produce items only when requested.
* They are memory efficient for large data streams.
* Created either by:

  * Generator functions (using `yield`)
  * Generator expressions (similar to list comprehensions but with parentheses)

---

# 2. **Generator Function Syntax**

```python
def generator_function():
    yield value1
    yield value2
    # ...
```

`yield` pauses the function saving its state and returns the value to the caller. When next item is requested, function resumes from after the last `yield`.

---

# 3. **Example: Simple Generator**

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

gen = count_up_to(5)
print(next(gen))  # 1
print(next(gen))  # 2
print(list(gen))  # [3, 4, 5]
```

---

# 4. **Difference between `yield` and `return`**

| Aspect          | `return`                      | `yield`                            |
| --------------- | ----------------------------- | ---------------------------------- |
| Function status | Ends the function immediately | Pauses and saves state             |
| Returns         | One value                     | Produces a sequence of values      |
| Function type   | Normal function               | Generator function                 |
| Memory          | Returns entire result at once | Lazy evaluation, values one by one |

---

# 5. **Generator Expressions**

Similar to list comprehensions but with parentheses.

```python
gen_exp = (x * x for x in range(5))
print(next(gen_exp))  # 0
print(list(gen_exp))  # [1, 4, 9, 16]
```

More memory efficient than list comprehensions, as they don’t create the entire list at once.

---

# 6. **Why Use Generators?**

* **Memory efficiency**: Only one item in memory at a time.
* **Represent infinite sequences**: E.g., infinite counting.
* **Pipeline processing**: Pass output of one generator to another.
* **Simplify code**: Generators can replace complex iterator classes.

---

# 7. **Generator Internals**

* Generator objects implement the iterator protocol (`__iter__()` and `__next__()`).
* When you call `next()` on a generator, the function runs until it hits `yield`, then pauses.
* When the function ends or `return` is encountered, it raises `StopIteration`.

---

# 8. **Example: Fibonacci Generator**

```python
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(7):
    print(num)
```

---

# 9. **Sending Values into Generators**

Generators can receive values back from the caller with `.send()`:

```python
def echo():
    while True:
        val = yield
        print(f"Received: {val}")

gen = echo()
next(gen)  # Prime the generator
gen.send("Hello")  # prints Received: Hello
```

This is an advanced feature often used in coroutines.

---

# 10. **Generator Close and Throw**

* `gen.close()` stops the generator and raises `GeneratorExit` inside.
* `gen.throw(ExceptionType)` injects an exception inside the generator.

---

# 11. **Difference Between Generators and Iterators**

| Aspect         | Generator                                | Iterator                                        |
| -------------- | ---------------------------------------- | ----------------------------------------------- |
| Creation       | Using generator functions or expressions | Created from iterable with `iter()` or manually |
| Implementation | Function with `yield` keyword            | Class implementing `__next__()`                 |
| Memory         | Lazy, produces values on demand          | May or may not be lazy                          |
| Syntax         | Simpler, no need for classes             | Usually more verbose                            |

---

# 12. **Example: Chaining Generators**

```python
def gen1():
    yield from range(3)

def gen2():
    yield from gen1()
    yield from range(3, 6)

for val in gen2():
    print(val)  # prints 0 to 5
```

---

# 13. **`yield from` Statement**

`yield from iterable` delegates part of the generator's operations to another iterable/generator.

Avoids writing nested loops manually, simplifies code.

---

# 14. **Use Cases**

* Reading large files line by line.
* Infinite data streams (e.g., sensor data).
* Data pipelines.
* Lazy evaluation in data science or web scraping.

---

# 15. **Summary Table**

| Feature             | Generator                                     | Iterator                             |
| ------------------- | --------------------------------------------- | ------------------------------------ |
| Created by          | Function with `yield` or generator expression | Class implementing `__next__()`      |
| Memory usage        | Lazy, very low                                | Depends on implementation            |
| Syntax complexity   | Simple, concise                               | Can be verbose                       |
| State preservation  | Automatic (function state saved)              | Must be manually managed             |
| Can receive input?  | Yes, via `.send()`                            | No                                   |
| Infinite sequences? | Easy to implement                             | Possible but requires careful design |

---

If you want, I can generate:

* Detailed code for advanced generators (with `send()`, `throw()`)
* Performance comparison examples between generators and list-based approaches
* Real-world examples with large data

Would you like me to proceed with those?

"""