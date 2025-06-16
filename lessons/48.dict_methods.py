"""
Here’s a **very detailed explanation of Python `dictionary` methods**, including their syntax, arguments, return types, edge cases, behaviors, and real-world usage.

---

## ✅ What is a `dictionary` in Python?

* A **dictionary (`dict`)** is a **mutable**, **unordered** (as of Python 3.7+, they preserve insertion order), **key-value** pair mapping.
* **Keys must be hashable** (i.e., immutable), and **values can be any type**.

---

## 🔹 Dictionary Creation

```python
d = {"a": 1, "b": 2}
d2 = dict(a=1, b=2)
d3 = dict([("x", 10), ("y", 20)])
d4 = {}                   # Empty dict
```

---

## ✅ Properties of Dict

| Feature               | Supported       |
| --------------------- | --------------- |
| Mutable               | ✅               |
| Ordered (3.7+)        | ✅               |
| Indexed               | ❌               |
| Keys must be unique   | ✅               |
| Duplicate keys        | ❌ Last one wins |
| Keys must be hashable | ✅               |

---

## ✅ Important Dictionary Methods (with in-depth detail)

---

### 🔹1. `get(key[, default])`

Returns value for `key` if present, else `default`.

```python
d = {"a": 1, "b": 2}
print(d.get("a"))         # 1
print(d.get("c"))         # None
print(d.get("c", 0))      # 0
```

* Doesn’t raise KeyError.
* Default is `None` if not specified.

---

### 🔹2. `keys()`

Returns a **view object** of all keys.

```python
d = {"x": 10, "y": 20}
print(d.keys())  # dict_keys(['x', 'y'])
```

> This object is **iterable** and updates dynamically with the dictionary.

---

### 🔹3. `values()`

Returns a **view object** of all values.

```python
d = {"x": 10, "y": 20}
print(d.values())  # dict_values([10, 20])
```

---

### 🔹4. `items()`

Returns view of all **(key, value)** tuples.

```python
d = {"x": 10, "y": 20}
print(d.items())  # dict_items([('x', 10), ('y', 20)])
```

> Often used for looping:

```python
for key, value in d.items():
    print(key, value)
```

---

### 🔹5. `update([other])`

Adds key-value pairs from `other`. Overwrites existing keys.

```python
d = {"a": 1}
d.update({"b": 2})
print(d)  # {'a': 1, 'b': 2}

d.update([("a", 10)])  # updates 'a'
print(d)  # {'a': 10, 'b': 2}
```

* Argument can be another dictionary or iterable of pairs.
* Also accepts keyword arguments:

```python
d.update(c=3)
```

---

### 🔹6. `copy()`

Returns a **shallow copy** of the dictionary.

```python
d1 = {"a": 1}
d2 = d1.copy()
d2["a"] = 2
print(d1, d2)  # {'a': 1} {'a': 2}
```

---

### 🔹7. `pop(key[, default])`

Removes and returns value for `key`.

* Raises `KeyError` if `key` not found and no `default` given.

```python
d = {"a": 1, "b": 2}
print(d.pop("a"))    # 1
print(d)             # {'b': 2}
print(d.pop("x", 0)) # 0
```

---

### 🔹8. `popitem()`

Removes and returns the **last inserted (key, value)** pair.

```python
d = {"a": 1, "b": 2}
print(d.popitem())   # ('b', 2)
```

* Raises `KeyError` if dict is empty.
* LIFO behavior (since Python 3.7).

---

### 🔹9. `setdefault(key[, default])`

If `key` exists, returns its value. If not, adds `key` with `default`.

```python
d = {"a": 1}
print(d.setdefault("a"))        # 1
print(d.setdefault("b", 10))    # 10
print(d)  # {'a': 1, 'b': 10}
```

> Useful for initializing nested dictionaries.

---

### 🔹10. `clear()`

Removes all items from the dictionary.

```python
d = {"a": 1}
d.clear()
print(d)  # {}
```

---

## ✅ Built-in Operations on Dicts

---

### 🔹11. `in` and `not in`

Test for presence of a key (not value!):

```python
d = {"x": 1}
print("x" in d)     # True
print(1 in d)       # False
```

---

### 🔹12. `len(dict)`

Returns number of key-value pairs.

```python
len({"a": 1, "b": 2})  # 2
```

---

### 🔹13. `del dict[key]`

Deletes a key explicitly:

```python
d = {"a": 1}
del d["a"]
print(d)  # {}
```

Raises `KeyError` if key is missing.

---

## ✅ Dictionary Comprehension

```python
squares = {x: x*x for x in range(5)}
print(squares)  # {0: 0, 1: 1, ..., 4: 16}
```

You can also use conditions:

```python
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
```

---

## ✅ Nested Dictionary Example

```python
students = {
    "John": {"math": 90, "sci": 85},
    "Amy": {"math": 92, "sci": 88}
}
print(students["Amy"]["sci"])  # 88
```

---

## ✅ Immutable Keys Only

Only **hashable (immutable)** keys allowed:

✅ Valid keys:

```python
d = {
  1: "int",
  "a": "str",
  (1, 2): "tuple"
}
```

❌ Invalid keys:

```python
d = {[1, 2]: "list"}  # ❌ TypeError: unhashable type
```

---

## ✅ Summary Table

| Method                     | Description                     |
| -------------------------- | ------------------------------- |
| `get(key, default)`        | Safe lookup with fallback       |
| `keys()`                   | View of all keys                |
| `values()`                 | View of all values              |
| `items()`                  | View of all key-value pairs     |
| `update(other)`            | Merge/update another dictionary |
| `copy()`                   | Shallow copy                    |
| `pop(key, default)`        | Remove key and return value     |
| `popitem()`                | Remove last inserted item       |
| `setdefault(key, default)` | Get or add key with default     |
| `clear()`                  | Remove all items                |

---

## 💡 Real-World Use Cases

* **JSON APIs**: Data received from web APIs is often in dict format.
* **Caching**: Dictionary can store expensive function results.
* **Frequency counters**:

  ```python
  freq = {}
  for ch in "hello":
      freq[ch] = freq.get(ch, 0) + 1
  ```

---

## ⚠️ Edge Cases

* Duplicate keys in literal: last wins.

```python
d = {"a": 1, "a": 2}
print(d)  # {'a': 2}
```

* You cannot use unhashable objects as keys.

---

## Bonus: `collections.defaultdict`

```python
from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)
d["b"].append(2)
print(d)  # defaultdict(<class 'list'>, {'a': [1], 'b': [2]})
```

---

Let me know if you want:

* Comparison: `dict` vs `list` vs `set`
* JSON vs Python dictionary handling
* Custom implementation of dictionary logic (hash tables)
* Task-based exercises for dict mastery

Shall we proceed to advanced usage or dive into data structures now?

"""