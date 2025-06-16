"""
Here is an extremely detailed explanation of **important Python `list` methods**, including what they do, arguments, optional parameters, return values, edge cases, and examples.

---

## ✅ Python List – Key Properties

* **Mutable**: You can change the content (add, remove, update elements).
* **Ordered**: Elements maintain the order in which they are added.
* **Can contain mixed data types**.

---

## 🔹1. `list.append(x)`

**Adds** an item `x` to the **end** of the list.

### Syntax:

```python
list.append(element)
```

### Arguments:

* `element`: Any valid Python object to be appended.

### Returns:

* `None` (modifies the list in-place)

### Example:

```python
lst = [1, 2, 3]
lst.append(4)
print(lst)  # [1, 2, 3, 4]
```

### Note:

* Appends as a **single object** (even if it's a list or tuple).

```python
lst.append([5, 6])
print(lst)  # [1, 2, 3, 4, [5, 6]]
```

---

## 🔹2. `list.extend(iterable)`

**Adds** all elements from an iterable to the **end** of the list.

### Syntax:

```python
list.extend(iterable)
```

### Arguments:

* `iterable`: A list, tuple, set, string, or any iterable.

### Returns:

* `None` (modifies the list in-place)

### Example:

```python
a = [1, 2]
a.extend([3, 4])
print(a)  # [1, 2, 3, 4]
```

### Difference from `append()`:

* `extend()` **unpacks** the iterable.
* `append()` adds the iterable **as a single element**.

---

## 🔹3. `list.insert(index, element)`

**Inserts** an element at a specific position.

### Syntax:

```python
list.insert(index, element)
```

### Arguments:

* `index`: Position to insert at.
* `element`: Object to insert.

### Returns:

* `None`

### Behavior:

* If `index > len(list)`, inserts at end.
* If `index < 0`, inserts at that offset from end.

### Example:

```python
lst = [1, 2, 3]
lst.insert(1, 99)
print(lst)  # [1, 99, 2, 3]
```

---

## 🔹4. `list.remove(x)`

**Removes** the **first occurrence** of element `x`.

### Syntax:

```python
list.remove(x)
```

### Arguments:

* `x`: The element to remove (must exist in the list).

### Returns:

* `None`

### Raises:

* `ValueError` if `x` not found.

### Example:

```python
a = [1, 2, 3, 2]
a.remove(2)
print(a)  # [1, 3, 2]
```

---

## 🔹5. `list.pop([index])`

**Removes and returns** the element at the given index. If no index, removes the last element.

### Syntax:

```python
list.pop()           # removes last
list.pop(index)      # removes at index
```

### Arguments:

* `index`: Optional integer index.

### Returns:

* The removed element.

### Raises:

* `IndexError` if list is empty or index out of range.

### Example:

```python
a = [10, 20, 30]
val = a.pop(1)
print(val)  # 20
print(a)    # [10, 30]
```

---

## 🔹6. `list.clear()`

**Removes all elements** from the list (empties it).

### Syntax:

```python
list.clear()
```

### Returns:

* `None`

### Example:

```python
a = [1, 2, 3]
a.clear()
print(a)  # []
```

---

## 🔹7. `list.index(x[, start[, end]])`

**Returns the index** of the first occurrence of value `x`.

### Syntax:

```python
list.index(x)
list.index(x, start)
list.index(x, start, end)
```

### Arguments:

* `x`: The value to search for.
* `start`: Optional; start index for the search.
* `end`: Optional; end index.

### Returns:

* Integer index

### Raises:

* `ValueError` if not found.

### Example:

```python
a = [5, 10, 15, 10]
print(a.index(10))        # 1
print(a.index(10, 2))     # 3
```

---

## 🔹8. `list.count(x)`

**Counts** the number of times `x` appears in the list.

### Syntax:

```python
list.count(x)
```

### Returns:

* Integer count

### Example:

```python
a = [1, 2, 2, 3, 2]
print(a.count(2))  # 3
```

---

## 🔹9. `list.sort(*, key=None, reverse=False)`

**Sorts** the list in-place.

### Syntax:

```python
list.sort()
list.sort(reverse=True)
list.sort(key=func)
```

### Arguments:

* `key`: Optional. Function to be used for sorting.
* `reverse`: Optional. Sort in descending order if `True`.

### Returns:

* `None`

### Example:

```python
a = [3, 1, 4]
a.sort()
print(a)  # [1, 3, 4]

a.sort(reverse=True)
print(a)  # [4, 3, 1]

# Using key
a = ['apple', 'banana', 'pear']
a.sort(key=len)
print(a)  # ['pear', 'apple', 'banana']
```

---

## 🔹10. `list.reverse()`

**Reverses** the list in-place.

### Syntax:

```python
list.reverse()
```

### Returns:

* `None`

### Example:

```python
a = [1, 2, 3]
a.reverse()
print(a)  # [3, 2, 1]
```

---

## 🔹11. `list.copy()`

**Returns a shallow copy** of the list.

### Syntax:

```python
new_list = old_list.copy()
```

### Returns:

* A new list with the same elements.

### Example:

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]
```

### Important:

* `copy()` creates a shallow copy → if the list contains mutable objects, both lists will share those.

---

## 🔹12. `list.__add__(list2)` (Operator `+`)

Combines two lists into a new one.

```python
a = [1, 2]
b = [3, 4]
c = a + b
print(c)  # [1, 2, 3, 4]
```

---

## 🔹13. `list.__mul__(n)` (Operator `*`)

Repeats the list `n` times.

```python
a = [1, 2]
print(a * 3)  # [1, 2, 1, 2, 1, 2]
```

---

## 🔹14. `in` / `not in` (Membership test)

```python
x = 3
a = [1, 2, 3]
print(x in a)      # True
print(x not in a)  # False
```

---

## ✅ Summary Table

| Method         | Purpose                        | Returns |
| -------------- | ------------------------------ | ------- |
| `append(x)`    | Add one element at end         | None    |
| `extend(iter)` | Add all elements from iterable | None    |
| `insert(i,x)`  | Insert at position `i`         | None    |
| `remove(x)`    | Remove first `x`               | None    |
| `pop([i])`     | Remove and return element      | Element |
| `clear()`      | Empty the list                 | None    |
| `index(x)`     | Get index of first `x`         | Int     |
| `count(x)`     | Count of `x`                   | Int     |
| `sort()`       | Sort the list                  | None    |
| `reverse()`    | Reverse the list               | None    |
| `copy()`       | Shallow copy                   | List    |

---

If you want:

* Internal memory explanation (mutability, object references)
* List comprehensions with logic
* Real-world coding tasks with solutions
* Advanced operations (slicing, nested lists, matrix ops)

Let me know, I can continue in that direction.

"""


"""
Here is a **very detailed explanation of important Python `tuple` methods and properties**, including usage, arguments, behaviors, edge cases, and examples — following the same deep-dive format as for strings and lists.

---

## ✅ What is a `tuple`?

* A **tuple** is an **ordered, immutable** sequence of elements.
* Tuples can hold **mixed data types**.
* They are **hashable** if all elements are hashable → can be used as dictionary keys or set members.

---

## 🔹 How to Create a Tuple

```python
t1 = (1, 2, 3)                 # normal tuple
t2 = ()                        # empty tuple
t3 = (1,)                      # single-element tuple (note comma)
t4 = tuple([1, 2, 3])          # using constructor
```

```python
type((1))    # <class 'int'>
type((1,))   # <class 'tuple'>
```

---

## 🔹 Properties of Tuples

| Property          | Value         |
| ----------------- | ------------- |
| Ordered           | ✅             |
| Mutable           | ❌ (immutable) |
| Allows Duplicates | ✅             |
| Indexable         | ✅             |
| Iterable          | ✅             |

---

## ✅ Important Tuple Methods

Tuples have **only two built-in methods**:

---

### 🔹1. `tuple.count(x)`

**Purpose**: Returns the number of times element `x` appears in the tuple.

### Syntax:

```python
tuple.count(x)
```

### Arguments:

* `x`: Value to count.

### Returns:

* Integer (number of times `x` appears).

### Example:

```python
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))  # Output: 3
print(t.count(5))  # Output: 0
```

---

### 🔹2. `tuple.index(x[, start[, end]])`

**Purpose**: Returns the index of the first occurrence of `x`. Optional range can be provided.

### Syntax:

```python
tuple.index(x)
tuple.index(x, start)
tuple.index(x, start, end)
```

### Arguments:

* `x`: Element to search.
* `start`: (Optional) Starting index.
* `end`: (Optional) Ending index (non-inclusive).

### Returns:

* Integer index

### Raises:

* `ValueError` if `x` is not found.

### Example:

```python
t = (10, 20, 30, 20, 40)
print(t.index(20))        # Output: 1
print(t.index(20, 2))     # Output: 3
print(t.index(50))        # ValueError: tuple.index(x): x not in tuple
```

---

## ✅ Other Operations Supported by Tuples

Even though tuples have only 2 methods, they support many **built-in operations**:

---

### 🔹3. Indexing

```python
t = (100, 200, 300)
print(t[0])   # 100
print(t[-1])  # 300
```

---

### 🔹4. Slicing

```python
t = (1, 2, 3, 4, 5)
print(t[1:4])    # (2, 3, 4)
print(t[::-1])   # (5, 4, 3, 2, 1)
```

---

### 🔹5. Iteration

```python
t = (10, 20, 30)
for item in t:
    print(item)
```

---

### 🔹6. `in` and `not in` (Membership test)

```python
t = (1, 2, 3)
print(2 in t)      # True
print(5 not in t)  # True
```

---

### 🔹7. Length

```python
len((1, 2, 3))  # 3
```

---

### 🔹8. Concatenation

```python
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2     # (1, 2, 3, 4)
```

---

### 🔹9. Repetition

```python
t = (1, 2)
print(t * 3)   # (1, 2, 1, 2, 1, 2)
```

---

### 🔹10. Nested Tuples

```python
t = ((1, 2), (3, 4))
print(t[1][0])   # 3
```

---

## 🔐 Immutability Explained

* You **cannot modify** a tuple once it’s created:

```python
t = (1, 2, 3)
t[0] = 10   # ❌ TypeError
```

* But you **can have mutable objects inside**:

```python
t = ([1, 2], 3)
t[0][0] = 999
print(t)  # ([999, 2], 3)
```

---

## ✅ Tuple Packing and Unpacking

```python
# Packing
t = 1, 2, 3    # tuple without parentheses
print(t)       # (1, 2, 3)

# Unpacking
a, b, c = t
print(a, b, c)  # 1 2 3
```

---

### 🔹 `*` Unpacking (Extended unpacking)

```python
a, *b = (1, 2, 3, 4)
print(a)  # 1
print(b)  # [2, 3, 4]
```

---

## 🔹 Conversion: `tuple()` constructor

```python
tuple([1, 2, 3])         # List → Tuple
tuple("abc")             # String → Tuple of chars
tuple((x for x in range(3)))  # Generator → Tuple
```

---

## 🔹 Summary Table

| Feature     | Supported in Tuple?         |
| ----------- | --------------------------- |
| `.count()`  | ✅ Yes                       |
| `.index()`  | ✅ Yes                       |
| `.append()` | ❌ No (immutable)            |
| `.remove()` | ❌ No                        |
| Slicing     | ✅ Yes                       |
| Indexing    | ✅ Yes                       |
| Mutability  | ❌ No                        |
| Hashable    | ✅ If all items are hashable |
| Unpacking   | ✅ Yes                       |
| Iteration   | ✅ Yes                       |

---

## 📌 Real-World Use-Cases

* Return multiple values from a function:

```python
def stats():
    return (mean, median, mode)
```

* Dictionary keys when using composite keys:

```python
my_dict = {(1, 2): "value"}
```

---

Let me know if you want:

* Tuple vs List vs Set vs Dict comparison table
* Memory usage comparison (tuples are smaller than lists)
* Interview MCQs or practice problems

I can also generate tasks based on this topic if you want.

"""

"""
Here is a **very detailed explanation of Python `set` methods**, including all arguments, optional parameters, return types, behavior, edge cases, and real-life use cases.

---

## ✅ What is a `set` in Python?

* A **set** is an **unordered**, **unindexed**, and **mutable** collection of **unique** elements.
* Duplicates are automatically removed.
* Sets are optimized for **fast membership testing** (`x in s`), and **set operations** like union, intersection, etc.

---

## 🔹 Set Creation

```python
s1 = {1, 2, 3}              # set literal
s2 = set([1, 2, 3])         # from list
s3 = set("hello")           # from string → {'o', 'h', 'e', 'l'}
s4 = set()                  # empty set (MUST use constructor)

type({})     # ⚠️ dict, not set!
```

---

## ✅ Important Set Methods (with very detailed explanation)

---

### 🔹1. `add(x)`

**Adds** an element `x` to the set (if not already present).

### Syntax:

```python
set.add(x)
```

### Arguments:

* `x`: Any hashable object.

### Returns:

* `None`

### Example:

```python
s = {1, 2}
s.add(3)
print(s)  # {1, 2, 3}
s.add(2)
print(s)  # {1, 2, 3} (no duplicate added)
```

---

### 🔹2. `update(iterable)`

**Adds all** elements from the iterable(s) to the set.

### Syntax:

```python
set.update(iterable1, iterable2, ...)
```

### Arguments:

* One or more iterables (list, set, tuple, string, etc.)

### Returns:

* `None`

### Example:

```python
s = {1, 2}
s.update([3, 4], (5, 6))
print(s)  # {1, 2, 3, 4, 5, 6}
```

---

### 🔹3. `remove(x)`

**Removes** `x` from the set. Raises `KeyError` if `x` not found.

### Syntax:

```python
set.remove(x)
```

### Example:

```python
s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}
s.remove(5)  # ❌ KeyError
```

---

### 🔹4. `discard(x)`

Same as `remove()`, but **does NOT raise error** if `x` is not found.

### Syntax:

```python
set.discard(x)
```

### Example:

```python
s = {1, 2}
s.discard(2)  # OK
s.discard(5)  # OK, no error
print(s)      # {1}
```

---

### 🔹5. `pop()`

**Removes and returns** an arbitrary element from the set.

### Syntax:

```python
set.pop()
```

### Returns:

* The removed element.

### Raises:

* `KeyError` if set is empty.

### Example:

```python
s = {1, 2, 3}
x = s.pop()
print(x, s)  # x is arbitrary
```

---

### 🔹6. `clear()`

**Removes all elements** from the set.

```python
s = {1, 2}
s.clear()
print(s)  # set()
```

---

### 🔹7. `copy()`

Returns a **shallow copy** of the set.

```python
s1 = {1, 2}
s2 = s1.copy()
s2.add(3)
print(s1)  # {1, 2}
print(s2)  # {1, 2, 3}
```

---

## ✅ Set Operations

All return new sets unless specified otherwise.

---

### 🔹8. `union(*others)` or `|`

Returns the **union** of the set with all others.

```python
a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}
print(a | b)       # {1, 2, 3}
```

---

### 🔹9. `intersection(*others)` or `&`

Returns common elements.

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}
print(a & b)              # {2, 3}
```

---

### 🔹10. `difference(*others)` or `-`

Returns items in the first set **not in** the others.

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))  # {1}
print(a - b)            # {1}
```

---

### 🔹11. `symmetric_difference(other)` or `^`

Returns items in **either** set but not both.

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))  # {1, 4}
print(a ^ b)                      # {1, 4}
```

---

## ✅ In-place Set Operations

These **modify** the original set:

| Method                                   | Description               |
| ---------------------------------------- | ------------------------- |
| `set.update(other)`                      | Union (in-place)          |
| `set.intersection_update(other)`         | Intersection (in-place)   |
| `set.difference_update(other)`           | Difference (in-place)     |
| `set.symmetric_difference_update(other)` | Symmetric diff (in-place) |

### Example:

```python
a = {1, 2, 3}
b = {2, 3, 4}
a.difference_update(b)
print(a)  # {1}
```

---

## ✅ Membership and Comparison

### 🔹 `in` / `not in`

```python
a = {1, 2, 3}
print(2 in a)      # True
print(4 not in a)  # True
```

### 🔹 Comparison Operators

| Operator | Meaning                     |
| -------- | --------------------------- |
| `a == b` | Equal sets                  |
| `a != b` | Not equal                   |
| `a < b`  | a is a proper subset of b   |
| `a <= b` | a is subset of b            |
| `a > b`  | a is a proper superset of b |
| `a >= b` | a is superset of b          |

---

### 🔹 Useful Boolean Methods

| Method            | Returns                              |
| ----------------- | ------------------------------------ |
| `a.isdisjoint(b)` | `True` if no common elements         |
| `a.issubset(b)`   | `True` if all elements of `a` in `b` |
| `a.issuperset(b)` | `True` if all elements of `b` in `a` |

### Example:

```python
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))     # True
print(b.issuperset(a))   # True
```

---

## ⚠️ Set Restrictions

* Elements must be **immutable** (hashable).

```python
s = {1, 2, [3, 4]}  # ❌ TypeError: unhashable type: 'list'
```

* Sets are **unordered** → no indexing or slicing.

```python
s = {1, 2, 3}
print(s[0])  # ❌ TypeError
```

---

## ✅ Frozenset (Immutable Set)

* `frozenset()` is like `set`, but immutable.
* Supports all **non-mutating** set operations.

```python
fs = frozenset([1, 2, 3])
# fs.add(4)  ❌ AttributeError: can't modify frozenset
```

---

## ✅ Summary Table

| Method                       | Description                       |                              |
| ---------------------------- | --------------------------------- | ---------------------------- |
| `add(x)`                     | Add one item                      |                              |
| `update(iterables)`          | Add multiple items                |                              |
| `remove(x)`                  | Remove item (error if not found)  |                              |
| `discard(x)`                 | Remove item (no error if missing) |                              |
| `pop()`                      | Remove and return arbitrary item  |                              |
| `clear()`                    | Remove all items                  |                              |
| `copy()`                     | Shallow copy                      |                              |
| \`union() /                  | \`                                | All unique items in all sets |
| `intersection() / &`         | Common items                      |                              |
| `difference() / -`           | Items in one not in others        |                              |
| `symmetric_difference() / ^` | Items in either, not both         |                              |
| `issubset(), issuperset()`   | Comparisons                       |                              |
| `isdisjoint()`               | True if sets have no common items |                              |

---

## 💡 Real-Life Use Cases

* **Remove duplicates** from list:

  ```python
  lst = [1, 2, 2, 3]
  unique = list(set(lst))
  ```

* **Common elements** between two lists:

  ```python
  common = set(a) & set(b)
  ```

* **Tags or categories**: Enforce uniqueness and fast lookups.

---

Let me know if you want:

* Comparison: `set` vs `list` vs `tuple`
* Visual diagrams of set operations
* Practice problems for set operations and logic
* Behind-the-scenes memory model for `set`

Ready to move to dictionaries next?

"""