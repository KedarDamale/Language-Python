"""
Alright, let's get straight to the point about the `del` keyword in Python — no fluff, just facts.

---

## What is `del` in Python?

* `del` is a **statement** (not a function).
* It is used to **delete objects**, **variables**, **items from collections** like lists, dictionaries, or slices.
* After using `del`, the reference to the object/variable/item is removed from the current namespace or container.
* If no other references to the object exist, Python's garbage collector will free the memory.

---

## Where and how can you use `del`?

### 1. Delete a variable (remove its binding)

```python
x = 10
print(x)  # Output: 10

del x
print(x)  # Raises NameError: name 'x' is not defined
```

* After `del x`, the variable `x` is removed from the current scope.
* Trying to access `x` afterward causes a `NameError`.

---

### 2. Delete an item in a list by index

```python
lst = [1, 2, 3, 4]
del lst[1]
print(lst)  # Output: [1, 3, 4]
```

* Deletes the item at index 1 (`2` in this case).
* List shrinks, and elements after that index shift left.

---

### 3. Delete a slice in a list

```python
lst = [0, 1, 2, 3, 4, 5]
del lst[2:5]
print(lst)  # Output: [0, 1, 5]
```

* Deletes multiple items in the specified slice.
* The list shrinks accordingly.

---

### 4. Delete a key-value pair in a dictionary

```python
d = {'a': 1, 'b': 2, 'c': 3}
del d['b']
print(d)  # Output: {'a': 1, 'c': 3}
```

* Removes the key `'b'` and its associated value.

---

### 5. Delete attributes of objects (if supported)

```python
class MyClass:
    def __init__(self):
        self.value = 10

obj = MyClass()
print(obj.value)  # 10

del obj.value
print(obj.value)  # AttributeError: 'MyClass' object has no attribute 'value'
```

* Deletes the attribute from the object.
* Accessing afterward throws `AttributeError`.

---

## Important details about `del`

* `del` **does not delete the object itself**; it deletes the reference/name to the object.
* If there are other references to the object elsewhere, the object will persist in memory.
* If no references remain, the object is garbage collected.
* `del` can delete multiple variables/items in one statement:

```python
a, b = 1, 2
del a, b
```

---

## What `del` is **NOT**:

* `del` is **not** like C/C++ `free()` or explicit memory deallocation.
* It does **not** forcibly destroy the object immediately; it just removes the reference.
* It's not a function, so you can't assign `del x` or use it in expressions.

---

## Summary in brief

| Usage                  | Effect                                  |
| ---------------------- | --------------------------------------- |
| `del variable`         | Removes variable binding from namespace |
| `del list[index]`      | Removes element at index                |
| `del list[start:end]`  | Removes slice of elements               |
| `del dict[key]`        | Removes key-value pair                  |
| `del object.attribute` | Removes attribute from object           |

---

If you want, I can show you **edge cases** or how `del` interacts with **namespaces and scopes** too. Let me know.

"""