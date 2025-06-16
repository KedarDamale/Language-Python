"""
Alright, here’s a detailed, technical explanation of Python’s `sorted()` function — its behavior, arguments, internal mechanism, and nuances.

---

# `sorted()` Function in Python — Detailed Explanation

`sorted()` is a built-in Python function used to **return a new sorted list from the elements of any iterable**. It does **not modify the original iterable** but produces a **new sorted list**.

---

## 1. Signature

```python
sorted(iterable, *, key=None, reverse=False)
```

Where:

* `iterable`: Any iterable (list, tuple, string, dict, generator, etc.) whose elements you want to sort.
* `key` (optional): A function that takes one argument and returns a value to be used for sorting comparison.
* `reverse` (optional): A boolean. If `True`, sorts in descending order. Default is `False` (ascending).

---

## 2. What does `sorted()` do?

* Takes all elements from the iterable.
* Uses the **Timsort algorithm** (hybrid stable sorting algorithm) to sort elements.
* Sorts elements by their natural order or by values returned from the `key` function.
* Returns a **new list** containing sorted elements.
* Original iterable remains unchanged.

---

## 3. Examples

### Basic sorting

```python
sorted([3, 1, 4, 2])  # [1, 2, 3, 4]
sorted("python")      # ['h', 'n', 'o', 'p', 't', 'y']
```

### Using `key` argument

Sort by length of strings:

```python
words = ["banana", "pie", "Washington", "book"]
sorted(words, key=len)  # ['pie', 'book', 'banana', 'Washington']
```

### Using `reverse=True`

```python
sorted([3, 1, 4, 2], reverse=True)  # [4, 3, 2, 1]
```

---

## 4. How does `sorted()` work internally?

* Internally, `sorted()` converts the input iterable into a list.
* Then it runs the **Timsort algorithm**, which is:

  * Stable (preserves order of equal elements).
  * Hybrid of merge sort and insertion sort.
  * Optimized for partially sorted data.
* If `key` is provided, `sorted()`:

  * Calls `key` function once per element.
  * Uses the results to compare elements instead of the original elements.
* If `reverse` is `True`, the list is reversed after sorting.

---

## 5. Arguments detailed

### `iterable`

* Any iterable is accepted.
* `sorted()` creates a list internally; so memory usage depends on iterable size.

### `key`

* Should be a callable that takes one argument.
* Returns a value used for sorting comparison.
* Examples: `key=len`, `key=str.lower`, `key=lambda x: x[1]`

### `reverse`

* Boolean flag.
* If `True`, reverses the final sorted list.
* Default is `False`.

---

## 6. Important characteristics

* **Stability**: `sorted()` is stable. Equal elements keep their relative order.
* **Return type**: Always returns a new **list**, regardless of the input type.
* **Original iterable unchanged**: Unlike `list.sort()`, which sorts in-place, `sorted()` never modifies the original data.
* **Supports custom classes**: If elements implement comparison operators (`__lt__`, etc.), they can be sorted.
* **TypeError**: If elements are not mutually comparable (e.g., mixing strings and ints), `TypeError` is raised.

---

## 7. Usage notes and examples

### Sorting dictionaries by keys or values

```python
d = {'a': 3, 'b': 1, 'c': 2}
sorted(d)              # ['a', 'b', 'c']  # sorts by keys
sorted(d.items(), key=lambda x: x[1])  # [('b', 1), ('c', 2), ('a', 3)]
```

### Sorting by multiple criteria (using tuple keys)

```python
students = [('Alice', 25), ('Bob', 20), ('Charlie', 25)]
sorted(students, key=lambda x: (x[1], x[0]))
# Sort by age, then name:
# [('Bob', 20), ('Alice', 25), ('Charlie', 25)]
```

---

## 8. Performance considerations

* Time complexity: **O(n log n)** average and worst case.
* Space complexity: Requires additional memory to create a list copy.
* For very large datasets, be mindful of memory usage.
* Timsort is optimized for real-world data and is very fast.

---

## 9. Comparison with `list.sort()`

| Feature           | `sorted()`                             | `list.sort()`                |
| ----------------- | -------------------------------------- | ---------------------------- |
| In-place sorting  | No (returns new list)                  | Yes (modifies original list) |
| Accepts iterables | Yes                                    | No (only lists)              |
| Return value      | New sorted list                        | `None`                       |
| Usage             | Useful when original data must be kept | Useful for in-place sorting  |

---

## 10. Summary Table

| Aspect            | Details                                            |
| ----------------- | -------------------------------------------------- |
| Return type       | New sorted list                                    |
| Arguments         | iterable, key (optional), reverse (optional)       |
| Sort algorithm    | Timsort (stable, hybrid merge/insertion sort)      |
| Sort order        | Ascending by default, descending if `reverse=True` |
| Key function      | Called once per element to determine sort key      |
| Original iterable | Not modified                                       |
| Performance       | O(n log n) time, extra memory for list copy        |

---

# TL;DR

* `sorted(iterable, key=None, reverse=False)` returns a **new list** with elements sorted.
* Uses a **stable Timsort algorithm** internally.
* Supports a custom **key function** and reverse sorting.
* Does **not modify** the original iterable.
* Works on any iterable, not just lists.

---

If you want, I can explain how Timsort works in detail or show you a Python-coded simplified sorting example. Want me to?

"""