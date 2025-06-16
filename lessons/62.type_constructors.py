"""
Let’s now **deep-dive into Python’s built-in type constructors**, which are used to create or convert between **fundamental data types**.

---

# 🔧 Python Built-in Type Constructors — Full Reference

Every data type in Python (like `int`, `float`, `list`, etc.) is actually a **class**, and calling that class like a function is how you construct or convert values.

---

### ✅ Format of a Type Constructor:

```python
TypeName([value])  # Optional or required value depending on type
```

---

Here’s a **complete table + detailed explanation of each constructor**, including:

* Parameters (arguments)
* Default values
* Behavior
* Edge cases

---

## 1. `int()` — Integer

### ✅ Syntax:

```python
int(x=0, base=10)
```

### ✅ Arguments:

* `x`: Number or string to convert.
* `base`: Only valid if `x` is a string. Specifies numeral base (2 to 36).

### ✅ Behavior:

* Converts floats to ints (by truncating).
* Converts strings in decimal/base-N form to integers.
* Defaults to `0` if no argument.

### ✅ Examples:

```python
int()             → 0
int(3.8)          → 3
int("1010", 2)    → 10
int("12", 8)      → 10
```

---

## 2. `float()` — Floating-Point Number

### ✅ Syntax:

```python
float(x=0.0)
```

### ✅ Arguments:

* `x`: Number or string.

### ✅ Behavior:

* Converts `int`, `str`, etc., to float.
* Supports scientific notation.

### ✅ Examples:

```python
float()           → 0.0
float("3.14")     → 3.14
float("1e3")      → 1000.0
```

---

## 3. `complex()` — Complex Number

### ✅ Syntax:

```python
complex(real=0.0, imag=0.0)
```

### ✅ Arguments:

* `real`: Real part.
* `imag`: Imaginary part or string.

### ✅ Behavior:

* Can accept single string like `"1+2j"` or two numeric parts.

### ✅ Examples:

```python
complex()               → 0j
complex(1, 2)           → (1+2j)
complex("3+4j")         → (3+4j)
```

---

## 4. `bool()` — Boolean

### ✅ Syntax:

```python
bool(x)
```

### ✅ Arguments:

* `x`: Any object.

### ✅ Behavior:

* Returns `False` for: `0`, `0.0`, `None`, `[]`, `{}`, `''`, `set()`, etc.
* Otherwise returns `True`.

### ✅ Examples:

```python
bool()        → False
bool(0)       → False
bool(1)       → True
bool("hi")    → True
```

---

## 5. `str()` — String

### ✅ Syntax:

```python
str(object='')
```

### ✅ Arguments:

* `object`: Anything — number, list, bool, etc.

### ✅ Behavior:

* Converts any object to its string representation.

### ✅ Examples:

```python
str()             → ''
str(10)           → '10'
str([1,2,3])      → '[1, 2, 3]'
```

---

## 6. `list()` — List

### ✅ Syntax:

```python
list(iterable=[])
```

### ✅ Arguments:

* `iterable`: Can be string, tuple, range, etc.

### ✅ Behavior:

* Converts iterable to a list.
* Empty call returns `[]`.

### ✅ Examples:

```python
list()               → []
list("abc")          → ['a', 'b', 'c']
list((1, 2, 3))       → [1, 2, 3]
```

---

## 7. `tuple()` — Tuple

### ✅ Syntax:

```python
tuple(iterable=[])
```

### ✅ Arguments:

* Same as `list()`.

### ✅ Behavior:

* Returns immutable sequence.

### ✅ Examples:

```python
tuple("abc")         → ('a', 'b', 'c')
tuple([1, 2, 3])     → (1, 2, 3)
```

---

## 8. `set()` — Set

### ✅ Syntax:

```python
set(iterable=[])
```

### ✅ Arguments:

* Iterable of hashable items.

### ✅ Behavior:

* Removes duplicates, unordered.

### ✅ Examples:

```python
set("aabc")          → {'a', 'b', 'c'}
set([1, 2, 2, 3])     → {1, 2, 3}
```

---

## 9. `frozenset()` — Immutable Set

### ✅ Syntax:

```python
frozenset(iterable=[])
```

### ✅ Behavior:

* Like `set()` but immutable.

### ✅ Examples:

```python
frozenset("hello")   → frozenset({'h', 'e', 'l', 'o'})
```

---

## 10. `dict()` — Dictionary

### ✅ Syntax:

```python
dict(mapping_or_iterable={}, **kwargs)
```

### ✅ Arguments:

* Can pass:

  * A `dict`
  * List of pairs: `[(k1, v1), (k2, v2)]`
  * Keyword args: `a=1, b=2`

### ✅ Examples:

```python
dict()                          → {}
dict(a=1, b=2)                  → {'a': 1, 'b': 2}
dict([('x', 9), ('y', 10)])     → {'x': 9, 'y': 10}
```

---

## 11. `bytes()` — Immutable Byte Sequence

### ✅ Syntax:

```python
bytes(source=0, encoding=None, errors='strict')
```

### ✅ Arguments:

* `source`: int (size), bytes, or iterable of ints.
* `encoding`: Required if source is `str`.

### ✅ Examples:

```python
bytes(4)              → b'\x00\x00\x00\x00'
bytes("AB", "utf-8")  → b'AB'
```

---

## 12. `bytearray()` — Mutable Byte Sequence

### ✅ Syntax:

```python
bytearray([source], encoding, errors)
```

### ✅ Behavior:

* Same as `bytes()` but mutable.

```python
bytearray("AB", "utf-8") → bytearray(b'AB')
```

---

## 13. `memoryview()` — View on bytes

### ✅ Syntax:

```python
memoryview(obj)
```

### ✅ Arguments:

* `obj`: Must support buffer protocol (`bytes`, `bytearray`, etc.)

### ✅ Examples:

```python
m = memoryview(b'hello')
m[0]           → 104  # ASCII of 'h'
```

---

## 14. `range()` — Sequence of Integers

### ✅ Syntax:

```python
range(start, stop[, step])
```

### ✅ Arguments:

* `start`: inclusive (default 0)
* `stop`: exclusive
* `step`: increment (default 1)

### ✅ Examples:

```python
range(5)        → [0,1,2,3,4]
range(1, 10, 2) → [1,3,5,7,9]
```

---

## 15. `enumerate()`, `zip()`, `reversed()`

| Function      | Purpose                                  |
| ------------- | ---------------------------------------- |
| `enumerate()` | Pairs index and value from iterable      |
| `zip()`       | Combines multiple iterables element-wise |
| `reversed()`  | Reverses a sequence                      |

### ✅ Example:

```python
enumerate(['a', 'b']) → (0, 'a'), (1, 'b')
zip([1,2],[3,4])      → (1,3), (2,4)
reversed("abc")       → 'c', 'b', 'a'
```

---

## 🧠 Summary Table

| Type       | Constructor    | Mutable | Notes                           |
| ---------- | -------------- | ------- | ------------------------------- |
| Integer    | `int()`        | ❌       | Truncates float; supports base  |
| Float      | `float()`      | ❌       | Converts string/number to float |
| Complex    | `complex()`    | ❌       | Supports real, imag, or string  |
| Boolean    | `bool()`       | ❌       | Truthy/falsy evaluation         |
| String     | `str()`        | ❌       | Universal to-string conversion  |
| List       | `list()`       | ✅       | Converts any iterable to list   |
| Tuple      | `tuple()`      | ❌       | Immutable list                  |
| Set        | `set()`        | ✅       | Unordered, no duplicates        |
| Frozenset  | `frozenset()`  | ❌       | Immutable set                   |
| Dict       | `dict()`       | ✅       | From mapping or iterable        |
| Bytes      | `bytes()`      | ❌       | Immutable byte string           |
| Bytearray  | `bytearray()`  | ✅       | Mutable version of bytes        |
| MemoryView | `memoryview()` | ✅       | Slice view on bytes             |
| Range      | `range()`      | ❌       | Efficient int sequence          |

---

Would you like **internal memory diagrams**, or **performance/time-complexity charts** for each constructor?

"""