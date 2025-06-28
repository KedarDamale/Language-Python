"""
### 🔍 What is *Unpacking* in Python?

**Unpacking in Python** refers to assigning elements of an iterable (like a list, tuple, or string) into multiple variables in a single statement. It's a clean and readable way to extract values from a container.

---

### ✅ Basic Tuple/List Unpacking

Suppose you have a tuple:

```python
data = (10, 20, 30)
a, b, c = data
```

* `a` gets `10`
* `b` gets `20`
* `c` gets `30`

This is called **tuple unpacking**.
Works similarly with lists:

```python
values = [1, 2, 3]
x, y, z = values
```

If the number of variables doesn't match the number of elements, Python throws a `ValueError`.

---

### ✅ Unpacking with `*` (Starred Expression)

You can use a **starred expression (`*`)** to unpack a variable number of items.

```python
a, *b = [1, 2, 3, 4, 5]
```

* `a = 1`
* `b = [2, 3, 4, 5]`

Another example:

```python
*a, b = [1, 2, 3, 4, 5]
```

* `a = [1, 2, 3, 4]`
* `b = 5`

Starred unpacking works only **once** in an unpacking expression.

---

### ✅ Practical Examples

#### 1. Swapping variables (without temp variable):

```python
x, y = 5, 10
x, y = y, x
```

#### 2. Splitting a full name:

```python
full_name = "Alan Mathison Turing"
first, *middle, last = full_name.split()
```

* `first = "Alan"`
* `middle = ["Mathison"]`
* `last = "Turing"`

#### 3. Ignoring certain values using `_`:

```python
data = (1, 2, 3, 4)
a, _, _, d = data
```

Common pattern when you want to ignore some values.

---

### ✅ Unpacking in Loops

```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

for num, char in pairs:
    print(f"{num} => {char}")
```

Each tuple in the list is unpacked into `num` and `char`.

---

### ✅ Dictionary Unpacking (`**`)

Used when calling a function with a dictionary of keyword arguments.

```python
def greet(name, age):
    print(f"Hello {name}, age {age}")

data = {'name': 'Alice', 'age': 30}
greet(**data)
```

Here `**data` unpacks the dictionary into `name='Alice', age=30`.

---

### ✅ Combined Use (`*args`, `**kwargs`)

Used in function definitions and calls:

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, name="Alice", age=25)
```

* `args` becomes `(1, 2, 3)` (tuple of positional arguments)
* `kwargs` becomes `{'name': 'Alice', 'age': 25}`

---

### 🔥 Advanced Example

```python
a, *b, c = range(10)
```

* `a = 0`
* `b = [1,2,3,4,5,6,7,8]`
* `c = 9`

Useful when you want to extract the head, tail, or last item of a sequence.

---

### 🔴 Common Errors

```python
a, b = [1, 2, 3]  # ❌ ValueError: too many values to unpack
```

To fix:

```python
a, *b = [1, 2, 3]  # ✅
```

---

### ✅ Summary

| Use Case                    | Syntax                    |
| --------------------------- | ------------------------- |
| Tuple/List unpacking        | `a, b = (1, 2)`           |
| Variable-length unpacking   | `a, *rest = [1, 2, 3]`    |
| Ignoring values             | `_, b = (1, 2)`           |
| Swapping                    | `a, b = b, a`             |
| Function call with dict     | `func(**my_dict)`         |
| Unpacking in loops          | `for a, b in iterable:`   |
| Function args/kwargs unpack | `def f(*args, **kwargs):` |

Let me know if you want unpacking with real-world problems or interview-level questions.

"""
