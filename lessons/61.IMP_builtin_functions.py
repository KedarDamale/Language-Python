"""
Here’s a detailed, no-nonsense explanation of the Python built-in function `abs()`.

---

# `abs()` Function in Python — Detailed Explanation

---

## 1. Purpose

`abs()` returns the **absolute value** of a number, which means it returns the **magnitude** without regard to sign (i.e., it makes negative numbers positive and leaves positive numbers unchanged).

---

## 2. Signature

```python
abs(x)
```

* **x**: A numeric value — can be an integer, floating-point number, or complex number.

---

## 3. Behavior by type of `x`

* **Integer (`int`)**: Returns the integer without sign.

  ```python
  abs(-10)  # returns 10
  abs(5)    # returns 5
  ```

* **Floating-point (`float`)**: Returns the positive float magnitude.

  ```python
  abs(-3.14)  # returns 3.14
  abs(2.718)  # returns 2.718
  ```

* **Complex number (`complex`)**: Returns the **magnitude** (also called modulus) — calculated as $\sqrt{real^2 + imag^2}$.

  ```python
  abs(3+4j)  # returns 5.0 because sqrt(3² + 4²) = 5
  ```

---

## 4. Under the hood — Implementation details

* In **CPython**, `abs()` is implemented as a C function in `Objects/abstract.c` (function `builtin_abs`).
* Internally, it:

  * Checks the type of `x`.
  * If `x` is a built-in numeric type (int, float, complex), it calls the corresponding C-level function to compute absolute value or magnitude.
  * If `x` is a user-defined object and implements a special method `__abs__()`, Python calls `x.__abs__()`.
  * Otherwise, it raises a `TypeError`.

---

## 5. Special method: `__abs__()`

* Any custom Python class can define its own behavior for `abs()` by implementing the `__abs__` method.
* Example:

  ```python
  class Vector:
      def __init__(self, x, y):
          self.x = x
          self.y = y
      def __abs__(self):
          return (self.x**2 + self.y**2)**0.5

  v = Vector(3, 4)
  print(abs(v))  # 5.0
  ```

---

## 6. Error cases

* If you pass a non-numeric, non-complex, non-abs-supporting object, Python raises:

  ```python
  TypeError: bad operand type for abs(): 'str'
  ```

---

## 7. Example usage

```python
print(abs(-7))           # 7
print(abs(3.14))         # 3.14
print(abs(-3.14))        # 3.14
print(abs(3 + 4j))       # 5.0
print(abs(0))            # 0

# Custom class example
class MyNumber:
    def __init__(self, val):
        self.val = val
    def __abs__(self):
        return abs(self.val)

print(abs(MyNumber(-10)))  # 10
```

---

## 8. Summary

| Input Type   | Output                                   |
| ------------ | ---------------------------------------- |
| `int`        | Integer absolute value                   |
| `float`      | Floating-point absolute value            |
| `complex`    | Magnitude (sqrt(real² + imag²)) as float |
| Custom class | Result of object's `__abs__()` method    |
| Others       | Raises `TypeError`                       |

---

# TL;DR

* `abs(x)` returns the **absolute value** (non-negative magnitude) of a number.
* Works with `int`, `float`, `complex`.
* Calls `x.__abs__()` if defined.
* Raises `TypeError` for unsupported types.

---

If you want, I can also explain **how absolute value is computed for complex numbers** mathematically or show you some performance aspects or implementation in C, just let me know.

"""

"""
Here’s a detailed, technical explanation of Python’s built-in `pow()` function — how it works, arguments, behavior, and use cases.

---

# `pow()` Function in Python — Detailed Explanation

---

## 1. Purpose

`pow()` computes the **power** of a number, i.e., it calculates:

$$
\text{pow}(x, y) = x^y
$$

Optionally, it can compute the power **modulo** a third argument efficiently:

$$
\text{pow}(x, y, z) = (x^y) \bmod z
$$

---

## 2. Signature

```python
pow(x, y, z=None)
```

* `x`: Base number (int, float, or other types supporting power)
* `y`: Exponent (int, float, or other compatible type)
* `z`: Optional modulus (must be an integer if provided)

---

## 3. Behavior

* If called as `pow(x, y)` (two arguments):

  * Returns $x^y$ computed **as `x` raised to the power `y`**.
  * Supports integer, float, and complex exponentiation.
* If called as `pow(x, y, z)` (three arguments):

  * Computes $(x^y) \bmod z$, **modular exponentiation**.
  * Only supports integers for `x`, `y`, and `z`.
  * Uses a fast, optimized algorithm (exponentiation by squaring).
  * More efficient than `(x ** y) % z` for large numbers.

---

## 4. Examples

### Basic power:

```python
pow(2, 3)       # 8  (2^3)
pow(4, 0.5)     # 2.0 (square root of 4)
pow(5, -1)      # 0.2 (reciprocal)
pow(2+3j, 2)    # (-5+12j) (complex exponentiation)
```

### Modular exponentiation:

```python
pow(2, 5, 13)   # (2^5) % 13 = 32 % 13 = 6
pow(10, 100, 7) # Efficient mod exponentiation
```

---

## 5. Under the hood — Implementation

* The built-in `pow()` is implemented in C for CPython (`bltinmodule.c`).
* When 3 arguments are provided, it uses **modular exponentiation** algorithm (exponentiation by squaring), which is:

  * Time complexity: $O(\log y)$
  * Memory efficient.
* For 2 arguments:

  * If exponent is integer, uses fast integer exponentiation.
  * For floats or complex numbers, calls relevant C math library functions.
* If any argument does not support the power operation, raises `TypeError`.

---

## 6. Restrictions

* When 3 arguments are provided:

  * `y` must be **non-negative integer**.
  * `x`, `y`, `z` must be integers.
* If `y` is negative or float with 3 args, Python raises `ValueError` or `TypeError`.

---

## 7. Use cases

* Calculating powers efficiently.
* Cryptography: Modular exponentiation (`pow(x, y, z)`) is widely used in RSA and other algorithms.
* Handling large exponents without overflow using modulus.
* Calculating roots and fractional powers using floating-point `y`.

---

## 8. Examples with edge cases

```python
pow(0, 0)       # returns 1 (by definition in Python)
pow(-2, 3)      # -8
pow(-2, 2)      # 4
pow(2, -3)      # 0.125 (float division)
pow(2, 3, 5)    # 3 (modular exponentiation)
pow(2, -3, 5)   # ValueError: pow() 3rd argument not allowed unless 2nd argument is non-negative integer
pow(2.0, 3)     # 8.0 (float output)
```

---

## 9. Comparison with `**` operator

* `x ** y` and `pow(x, y)` are mostly equivalent.
* Only `pow()` supports the **third modulus argument**.
* `pow()` is a function, so it can be passed as a callable.

---

## 10. Summary

| Arguments      | Behavior                                           |
| -------------- | -------------------------------------------------- |
| `pow(x, y)`    | Returns $x^y$                                      |
| `pow(x, y, z)` | Returns $(x^y) \bmod z$ efficiently (integer only) |

---

# TL;DR

* `pow(x, y)` = $x^y$, supports int, float, complex.
* `pow(x, y, z)` = $(x^y) \bmod z$, efficient modular exponentiation (integers only).
* Use 3-arg `pow()` for big numbers and cryptographic tasks.

---

If you want, I can provide you with the **pure Python implementation of modular exponentiation**, or examples demonstrating performance differences between `pow()` and `**` with modulus. Just say the word.

"""

"""
Here’s a detailed technical explanation of the Python built-in function `len()` — how it works, arguments, behavior, and implementation details.

---

# `len()` Function in Python — Detailed Explanation

---

## 1. Purpose

`len()` returns the **number of items** in an object — typically the length of a sequence (like string, list, tuple) or the number of keys in a collection (like dict, set).

---

## 2. Signature

```python
len(s)
```

* **s**: An object that supports the length protocol (has a length).

---

## 3. Supported types

`len()` works with:

* **Sequences**: `str`, `list`, `tuple`, `range`, `bytes`, `bytearray`, etc.
* **Collections**: `dict`, `set`, `frozenset`
* **Custom objects** that implement the `__len__()` special method.

---

## 4. How it works — Under the hood

* When you call `len(s)`, Python internally calls the **special method**:

  ```python
  s.__len__()
  ```

* This method must return a **non-negative integer**.

* If `s` does not implement `__len__()`, Python raises:

  ```python
  TypeError: object of type 'X' has no len()
  ```

---

## 5. Implementation details

* `len()` is a **built-in function implemented in C** in CPython.
* It dispatches to the object’s length slot in the C API (`sq_length` for sequences or `mp_length` for mappings).
* This means calling `len()` is very efficient — O(1) for most built-in types (length is stored internally).
* For custom classes, your `__len__()` can be any logic but should run efficiently.

---

## 6. Example usage

```python
print(len("Hello"))            # 5
print(len([1, 2, 3, 4, 5]))   # 5
print(len((10, 20)))           # 2
print(len({'a': 1, 'b': 2}))  # 2
print(len({1, 2, 3, 4}))       # 4
print(len(range(10)))          # 10
```

---

## 7. Custom class with `__len__()`

You can define your own class to support `len()` by implementing `__len__()`:

```python
class MyCollection:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return len(self.data)

c = MyCollection([1, 2, 3])
print(len(c))  # 3
```

---

## 8. Edge cases

* **Empty containers** return 0.

  ```python
  len([])     # 0
  len("")     # 0
  ```

* Passing a **non-length supporting object** raises `TypeError`:

  ```python
  len(100)  # TypeError: object of type 'int' has no len()
  ```

* Length must always be **non-negative**. Returning a negative value from `__len__()` in custom class raises `ValueError`.

---

## 9. Performance

* `len()` is **O(1)** for built-in containers because they store length internally.
* For custom classes, performance depends on `__len__()` implementation.

---

## 10. Summary

| Aspect               | Detail                                         |
| -------------------- | ---------------------------------------------- |
| Input                | Object with `__len__()` method                 |
| Output               | Non-negative integer (length)                  |
| Commonly used with   | `str`, `list`, `tuple`, `dict`, `set`, `range` |
| Error if unsupported | `TypeError`                                    |
| Internal mechanism   | Calls object's `__len__()`                     |

---

# TL;DR

* `len(s)` returns the number of items in `s`.
* Internally calls `s.__len__()`.
* Works with built-in sequences and collections, or any class implementing `__len__()`.
* Raises `TypeError` if `s` has no length.
* Always returns a non-negative integer.

---

If you want, I can show you how `len()` is implemented for some built-in types in C or provide examples of custom classes and edge cases.

"""

"""
Here’s a detailed, technical explanation of the Python built-in function `reversed()` — what it does, how it works, arguments, and internals.

---

# `reversed()` Function in Python — Detailed Explanation

---

## 1. Purpose

`reversed()` returns an **iterator** that yields the elements of a sequence or iterable **in reverse order**.

---

## 2. Signature

```python
reversed(seq)
```

* **seq**: A **sequence** or an object implementing the `__reversed__()` method or the sequence protocol (`__len__()` and `__getitem__()`).

---

## 3. Behavior

* Returns a **reverse iterator** object.
* Does **not** return a reversed copy — it creates an iterator that yields elements from the end to the start lazily (one by one).
* Works with sequences that support random access (`__getitem__`) and length (`__len__`).
* If the object implements `__reversed__()`, Python calls that method instead of using the default reversal.

---

## 4. Under the hood

* When you call `reversed(seq)`:

  * If `seq` implements `__reversed__()`, Python calls `seq.__reversed__()` and returns the iterator from that.
  * Otherwise, if `seq` supports sequence protocol (`__len__()` and `__getitem__()`), Python creates a reverse iterator that:

    * Starts from index `len(seq) - 1`.
    * Decrements index by 1 on each iteration.
    * Calls `seq[i]` for each `i` in reverse.
  * If neither condition is met, it raises `TypeError`.

---

## 5. Requirements for `seq`

* Must be a sequence with:

  * `__len__()` returning length.
  * `__getitem__()` supporting integer indexing from 0 to length-1.
* Or must have `__reversed__()` method returning an iterator.

---

## 6. Example usage

```python
# Using reversed on a list
lst = [1, 2, 3, 4]
for x in reversed(lst):
    print(x)
# Output:
# 4
# 3
# 2
# 1

# Using reversed on a string
for ch in reversed("hello"):
    print(ch)
# Output:
# o
# l
# l
# e
# h

# Using reversed with list comprehension
rev_list = [*reversed([10, 20, 30])]  # [30, 20, 10]

# Using reversed on a custom class implementing __reversed__
class MySeq:
    def __reversed__(self):
        yield 3
        yield 2
        yield 1

for x in reversed(MySeq()):
    print(x)
# Output:
# 3
# 2
# 1
```

---

## 7. Error cases

* Passing a non-sequence/non-reversible object raises:

```python
TypeError: 'X' object is not reversible
```

Example:

```python
reversed(10)  # TypeError: 'int' object is not reversible
```

---

## 8. Comparison with slicing

* You can also reverse sequences using slicing:

```python
lst[::-1]
```

* This creates a **reversed copy** of the sequence.
* `reversed()` returns an **iterator** without copying.
* `reversed()` is more memory-efficient for large sequences.

---

## 9. Performance

* `reversed()` is **O(1)** to create the iterator.
* Each iteration is **O(1)**, indexing elements backward.
* More efficient than copying and then reversing.

---

## 10. Summary

| Feature                 | Detail                                                            |
| ----------------------- | ----------------------------------------------------------------- |
| Input                   | Sequence with `__len__()` and `__getitem__()` or `__reversed__()` |
| Output                  | Reverse iterator (lazy)                                           |
| Does not modify input   | Yes                                                               |
| Raises on invalid input | `TypeError`                                                       |
| Efficient               | Yes, no copy unless you convert iterator                          |

---

# TL;DR

* `reversed(seq)` returns an iterator over `seq` in reverse order.
* Works on sequences or objects with `__reversed__()`.
* Efficient — no new reversed copy, just an iterator.
* Raises `TypeError` if input is not reversible.

---

If you want, I can explain how to implement `__reversed__()` in your own class or demonstrate difference between `reversed()` and slicing for various data types.

| Feature                         | `list.reverse()`                                   | `reversed()`                                                                                                      |
| ------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Type**                        | Method of list objects                             | Built-in function                                                                                                 |
| **Mutability / Effect on list** | Modifies the original list **in-place**            | Does **not** modify the original iterable                                                                         |
| **Return value**                | Returns `None` (modifies in-place)                 | Returns a **reverse iterator** over the iterable                                                                  |
| **Input types**                 | Only works on `list` objects                       | Works on any **sequence** or object implementing `__reversed__()` or sequence protocol (`__len__`, `__getitem__`) |
| **Memory usage**                | No additional memory needed beyond the list itself | Uses constant memory; iterator yields items lazily                                                                |
| **Usability**                   | Changes the list order permanently                 | Can be used for temporary reverse iteration                                                                       |
| **Copy created?**               | No                                                 | No (unless you convert iterator to list explicitly)                                                               |
| **Typical use case**            | When you want to permanently reverse a list        | When you want to iterate over an iterable backward without modifying it                                           |
| **Syntax example**              | `mylist.reverse()`                                 | `for x in reversed(mylist):`                                                                                      |
| **Chaining**                    | Cannot chain (returns `None`)                      | Can chain as it returns an iterator                                                                               |
| **Supports non-list iterables** | No                                                 | Yes (tuples, strings, ranges, custom objects)                                                                     |
| **Speed**                       | Very fast in-place operation (O(n))                | Efficient iterator, O(1) to create, O(1) per item                                                                 |


"""

"""
Here’s a detailed, technical explanation of Python’s built-in `all()` and `any()` functions — their behavior, arguments, working, internals, and use cases.

---

# `all()` and `any()` Functions in Python — Detailed Explanation

---

## 1. Purpose

* **`all(iterable)`**: Returns `True` if **all elements** in the iterable are truthy (or iterable is empty). Returns `False` if **any element is falsy**.
* **`any(iterable)`**: Returns `True` if **any element** in the iterable is truthy. Returns `False` if **all elements are falsy** (or iterable is empty).

These are often used for boolean condition checks across multiple values.

---

## 2. Signature

```python
all(iterable)
any(iterable)
```

* Both accept a **single argument**: an iterable (list, tuple, generator, etc.).

---

## 3. Arguments

* `iterable`: Any iterable Python object (list, tuple, dict, set, generator, etc.).
* Elements inside can be of any type, but their **truthiness** is tested using Python’s `bool()` conversion rules.

---

## 4. Behavior in detail

### 4.1. `all(iterable)`

* Iterates over each element in `iterable`.
* For each element `x`, evaluates `bool(x)`:

  * If `bool(x) is False` (i.e., the element is falsy), `all()` **immediately returns `False`** (short-circuit).
  * If none of the elements are falsy, after complete iteration it returns `True`.
* Special case: If the iterable is **empty**, `all()` returns `True` (vacuous truth).

### 4.2. `any(iterable)`

* Iterates over each element in `iterable`.
* For each element `x`, evaluates `bool(x)`:

  * If `bool(x) is True` (i.e., the element is truthy), `any()` **immediately returns `True`** (short-circuit).
  * If none of the elements are truthy, after complete iteration it returns `False`.
* Special case: If the iterable is **empty**, `any()` returns `False`.

---

## 5. Under the hood — Implementation details

* Both are implemented in C in CPython (inside `bltinmodule.c`).
* Both use **short-circuit evaluation**:

  * `all()` stops at first falsy element.
  * `any()` stops at first truthy element.
* Internally, they call `PyObject_IsTrue` on each element to check truthiness.
* Efficient for large or infinite iterables because of short-circuiting.

---

## 6. Truthiness in Python

Python treats values as **truthy** or **falsy** according to the following rules:

* Falsy values include:

  * `False`
  * `None`
  * Numeric zero of all types: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
  * Empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`
* Everything else is considered **truthy**.

Example:

```python
bool(0)     # False
bool("")    # False
bool([])    # False
bool(1)     # True
bool("abc") # True
```

---

## 7. Examples

### `all()` examples

```python
all([True, True, True])            # True
all([1, 2, 3, 0])                 # False (0 is falsy)
all([])                           # True (empty iterable)
all([1, "abc", [0], True])        # True (all truthy)
all([1, "", 3])                   # False ("" is falsy)
all([x > 0 for x in [1, 2, 3]])  # True (all > 0)
all([x > 0 for x in [1, 0, 3]])  # False (0 > 0 is False)
```

### `any()` examples

```python
any([False, False, True])         # True
any([0, "", None])                # False (all falsy)
any([])                          # False (empty iterable)
any([0, "", 1])                  # True (1 is truthy)
any([x < 0 for x in [1, -2, 3]]) # True (-2 < 0 is True)
any([x < 0 for x in [1, 2, 3]])  # False (all False)
```

---

## 8. Use cases

* Checking if **all** conditions in a list/generator are true (e.g., validating input).
* Checking if **any** condition is true (e.g., feature flags, permission checks).
* Replacing explicit loops with concise expressions.
* Working with generators to avoid evaluating all elements.

---

## 9. Differences and similarities

| Aspect                    | `all()`                                | `any()`                       |
| ------------------------- | -------------------------------------- | ----------------------------- |
| Returns                   | `True` if all elements truthy or empty | `True` if any element truthy  |
| Returns if empty iterable | `True` (vacuous truth)                 | `False`                       |
| Short-circuit condition   | Stops on first falsy element           | Stops on first truthy element |
| Typical use case          | Verify all conditions met              | Verify any condition met      |

---

## 10. Performance considerations

* Both functions have **O(n)** worst-case complexity, but short-circuiting can make them effectively O(1) if condition met early.
* Works well with **lazy iterables/generators** since iteration stops as soon as possible.

---

## 11. Summary

| Function | Input    | Returns                            | Short-circuits on    | Empty iterable return |
| -------- | -------- | ---------------------------------- | -------------------- | --------------------- |
| `all()`  | Iterable | `True` if all truthy, else `False` | First falsy element  | `True`                |
| `any()`  | Iterable | `True` if any truthy, else `False` | First truthy element | `False`               |

---

# TL;DR

* `all(iterable)`: Are **all elements truthy**? Returns `True` if yes or iterable empty.
* `any(iterable)`: Is **any element truthy**? Returns `True` if yes.
* Both short-circuit to improve efficiency.
* Work on any iterable with boolean evaluation.

---

If you want, I can provide you with:

* Custom implementations of `all()` and `any()`
* Examples using generators or real-world scenarios
* Explanation of short-circuiting with step-by-step iteration trace

Just ask.

"""

"""
Here’s a **very detailed, technical explanation** of Python’s built-in functions `max()` and `min()` covering their purpose, signature, arguments, behavior, internals, and examples.

---

# `max()` and `min()` Functions in Python — Detailed Explanation

---

## 1. Purpose

* `max()` returns the **largest item** in an iterable or the largest of two or more arguments.
* `min()` returns the **smallest item** in an iterable or the smallest of two or more arguments.

They are used to find extremum values efficiently.

---

## 2. Signatures

Two calling conventions each:

```python
max(iterable, *[, key, default])
max(arg1, arg2, *args, *[, key])
min(iterable, *[, key, default])
min(arg1, arg2, *args, *[, key])
```

---

## 3. Arguments and Parameters

* **`iterable`**: A single iterable (list, tuple, set, etc.) containing comparable elements.
* **`arg1, arg2, *args`**: Two or more positional arguments, each a value to compare.
* **`key` (optional)**: A function applied to each item for comparison (like in `sorted()`).
* **`default` (optional, only when passing iterable)**: Value returned if the iterable is empty, instead of raising `ValueError`.

---

## 4. Behavior and Working

### 4.1. Calling with multiple arguments

* `max(a, b, c, ...)` compares all arguments directly and returns the largest.
* `min(a, b, c, ...)` returns the smallest.
* All arguments must be comparable with each other, or `TypeError` is raised.

### 4.2. Calling with an iterable

* `max(iterable)` and `min(iterable)` iterate through the iterable, apply the optional `key` function to each item, and determine the extremum by comparing keys.

* If iterable is empty and `default` is not provided, raises:

  ```python
  ValueError: max() arg is an empty sequence
  ```

* If `default` is provided, it is returned instead of raising an exception.

### 4.3. Key function

* `key` is a callable applied to each element before comparison.
* Comparison uses `key(element)` values.
* This allows custom sorting criteria.

---

## 5. Under the hood — Implementation details

* Implemented in C (CPython).
* The algorithm:

  1. Initialize `extremum` to first element (or default if provided).
  2. Iterate elements, compute `key(element)` if `key` is given.
  3. Compare current element’s key with current `extremum` key.
  4. Replace `extremum` if necessary.
* For multiple args, compares each argument directly.
* Uses Python’s rich comparison methods (`__lt__`, `__gt__`).

---

## 6. Examples

### Without key

```python
max(3, 5, 1, 7)              # 7
min([10, 2, 30, 4])          # 2
max("banana")                # 'n' (max by ASCII value)
min("apple")                 # 'a'
```

### With `key`

```python
words = ["apple", "banana", "cherry", "date"]

max(words, key=len)          # "banana" (longest word)
min(words, key=len)          # "date" (shortest word)
```

### With empty iterable and default

```python
max([], default=0)           # 0 instead of ValueError
min([], default="none")      # "none"
```

---

## 7. Errors

* If no arguments passed: `TypeError`.
* If iterable empty and no default: `ValueError`.
* If elements not comparable: `TypeError`.

---

## 8. Performance

* Time complexity: **O(n)** — must check all elements once.
* Space complexity: **O(1)** — keeps track of one extremum and key value.

---

## 9. Differences between `max()` and `min()`

| Feature                  | `max()`                                  | `min()`                                  |
| ------------------------ | ---------------------------------------- | ---------------------------------------- |
| Returns                  | Largest element                          | Smallest element                         |
| Raises on empty iterable | `ValueError` (unless `default` provided) | `ValueError` (unless `default` provided) |
| Arguments                | Iterable or multiple positional          | Iterable or multiple positional          |
| Accepts `key` function   | Yes                                      | Yes                                      |
| Usage with strings       | Returns max/min character by ASCII       | Returns max/min character by ASCII       |

---

## 10. Summary Table

| Aspect                                   | `max()`                   | `min()`                   |
| ---------------------------------------- | ------------------------- | ------------------------- |
| Input                                    | Iterable or multiple args | Iterable or multiple args |
| Output                                   | Maximum value             | Minimum value             |
| Optional `key` param                     | Yes                       | Yes                       |
| Optional `default` param                 | Yes (for empty iterable)  | Yes (for empty iterable)  |
| Raises on empty iterable without default | `ValueError`              | `ValueError`              |
| Uses Python rich comparisons             | Yes                       | Yes                       |

---

# TL;DR

* `max()` returns the largest item; `min()` returns the smallest.
* Works with either an iterable or multiple arguments.
* Accepts a `key` function to customize comparisons.
* Raises `ValueError` on empty iterable unless `default` is provided.
* Runs in linear time O(n).

---

If you want, I can provide example code snippets showing advanced usage, or show how `key` affects the result in edge cases.

"""

"""

"""