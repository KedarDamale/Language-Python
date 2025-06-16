"""
Here’s a **very detailed explanation** of the most important Python string methods. This covers what each method does, their required and optional arguments, return types, behaviors, and caveats.

---

## 🔹1. `str.upper()`

**Purpose**: Converts all characters to uppercase.

**Syntax**:

```python
string.upper()
```

**Returns**: A new string with all characters in uppercase.

**Arguments**: None

**Note**: Original string remains unchanged (strings are immutable).

**Example**:

```python
"hello".upper()  # Output: "HELLO"
```

---

## 🔹2. `str.lower()`

**Purpose**: Converts all characters to lowercase.

**Syntax**:

```python
string.lower()
```

**Returns**: A new string with all characters in lowercase.

**Arguments**: None

**Example**:

```python
"HELLO".lower()  # Output: "hello"
```

---

## 🔹3. `str.title()`

**Purpose**: Converts the first character of every word to uppercase, rest lowercase.

**Syntax**:

```python
string.title()
```

**Example**:

```python
"hello world".title()  # Output: "Hello World"
```

**Caveat**: Words with apostrophes are handled oddly:

```python
"he's here".title()  # Output: "He'S Here"
```

---

## 🔹4. `str.capitalize()`

**Purpose**: Capitalizes only the first character of the entire string.

**Syntax**:

```python
string.capitalize()
```

**Example**:

```python
"hello world".capitalize()  # Output: "Hello world"
```

---

## 🔹5. `str.strip([chars])`

**Purpose**: Removes leading and trailing characters. Defaults to whitespace.

**Syntax**:

```python
string.strip()             # removes whitespace
string.strip(chars)        # removes specified characters
```

**Arguments**:

* `chars`: Optional. A string of characters to remove.

**Example**:

```python
"  hello  ".strip()       # "hello"
"$$hello$$".strip('$')    # "hello"
```

---

## 🔹6. `str.lstrip([chars])` & `str.rstrip([chars])`

**Purpose**: `lstrip()` removes from the left, `rstrip()` from the right.

**Example**:

```python
"  hello  ".lstrip()      # "hello  "
"  hello  ".rstrip()      # "  hello"
```

---

## 🔹7. `str.replace(old, new, count=-1)`

**Purpose**: Replace substrings.

**Syntax**:

```python
string.replace(old, new)             # replace all
string.replace(old, new, count)      # replace first `count` occurrences
```

**Arguments**:

* `old`: Required. The substring to replace.
* `new`: Required. The replacement string.
* `count`: Optional. Number of occurrences to replace.

**Example**:

```python
"banana".replace("a", "o", 2)  # Output: "bonona"
```

---

## 🔹8. `str.split(sep=None, maxsplit=-1)`

**Purpose**: Splits string into a list by a separator.

**Syntax**:

```python
string.split()                    # by whitespace
string.split(sep)                 # by custom separator
string.split(sep, maxsplit)       # with a max number of splits
```

**Returns**: A list of substrings.

**Example**:

```python
"apple,banana,grape".split(',')        # ['apple', 'banana', 'grape']
"apple banana grape".split(maxsplit=1)  # ['apple', 'banana grape']
```

---

## 🔹9. `str.join(iterable)`

**Purpose**: Joins elements of an iterable (e.g., list) with the string as a separator.

**Syntax**:

```python
sep.join(iterable)
```

**Example**:

```python
"-".join(["a", "b", "c"])  # Output: "a-b-c"
```

**Caution**: Only works with strings:

```python
",".join([1, 2, 3])  # TypeError
```

---

## 🔹10. `str.find(sub, start=0, end=len(str))`

**Purpose**: Returns index of first occurrence of substring or -1.

**Syntax**:

```python
string.find(sub)
string.find(sub, start)
string.find(sub, start, end)
```

**Returns**: Integer (index) or -1

**Example**:

```python
"hello world".find("world")       # Output: 6
"hello world".find("x")           # Output: -1
```

---

## 🔹11. `str.index(sub, start=0, end=len(str))`

**Purpose**: Same as `find()` but raises an error if not found.

**Syntax & Example**:

```python
"hello".index("e")    # 1
"hello".index("x")    # ValueError
```

---

## 🔹12. `str.startswith(prefix[, start[, end]])`

**Purpose**: Checks if the string starts with the given prefix.

**Syntax**:

```python
string.startswith(prefix)
string.startswith(prefix, start)
string.startswith(prefix, start, end)
```

**Returns**: Boolean

**Example**:

```python
"banana".startswith("ba")     # True
"banana".startswith("a", 1)   # True
```

---

## 🔹13. `str.endswith(suffix[, start[, end]])`

**Similar to `startswith()`**, but for end of string.

**Example**:

```python
"banana".endswith("na")     # True
```

---

## 🔹14. `str.count(sub[, start[, end]])`

**Purpose**: Returns the number of occurrences of substring.

**Example**:

```python
"banana".count("a")       # 3
"banana".count("na")      # 2
```

---

## 🔹15. `str.isalpha()`

**Purpose**: Checks if all characters are alphabetic (A-Z, a-z).

**Returns**: Boolean

**Example**:

```python
"hello".isalpha()     # True
"hello1".isalpha()    # False
```

---

## 🔹16. `str.isdigit()` / `str.isnumeric()` / `str.isdecimal()`

| Method        | Meaning                                      |
| ------------- | -------------------------------------------- |
| `isdigit()`   | Checks digits 0-9 and Unicode digits         |
| `isnumeric()` | Includes all numeric characters (¼, ⅓, etc.) |
| `isdecimal()` | Only 0-9, no fractions or superscripts       |

---

## 🔹17. `str.islower()` / `str.isupper()`

**Checks if all cased characters are lower or upper respectively.**

```python
"abc".islower()   # True
"ABC".isupper()   # True
```

---

## 🔹18. `str.zfill(width)`

**Purpose**: Pads the string with zeros from the left to reach `width`.

**Example**:

```python
"42".zfill(5)  # Output: "00042"
```

---

## 🔹19. `str.center(width, fillchar=' ')`

**Centers the string in a field of `width`, filled with `fillchar`.**

```python
"hi".center(10, '*')  # Output: "****hi****"
```

---

## 🔹20. `str.partition(sep)` / `str.rpartition(sep)`

**Splits string at first (`partition`) or last (`rpartition`) occurrence of separator into a 3-tuple:**

```python
"hello world".partition(" ")   # ('hello', ' ', 'world')
"hello world".rpartition(" ")  # ('hello', ' ', 'world')
```

---

## 🔹21. `str.encode(encoding='utf-8', errors='strict')`

**Returns a bytes version of the string.**

```python
"hello".encode()  # b'hello'
```

---

## 🔹22. `str.format(*args, **kwargs)`

**Purpose**: Advanced string formatting.

```python
"Hello, {}".format("World")           # Positional
"Name: {name}".format(name="Kedar")  # Keyword
```

---

## 🔹23. `str.casefold()`

**Aggressive version of `lower()`, used for caseless comparisons.**

```python
"straße".casefold() == "strasse"  # True
```

---

## Summary Table:

| Method                      | Purpose                        |
| --------------------------- | ------------------------------ |
| `upper/lower`               | Case conversion                |
| `title/capitalize/casefold` | Title or sentence style casing |
| `strip/lstrip/rstrip`       | Trim characters                |
| `replace`                   | Replace substrings             |
| `split/join`                | Tokenization and joining       |
| `find/index`                | Search substrings              |
| `count`                     | Count substrings               |
| `startswith/endswith`       | Match prefixes/suffixes        |
| `is...` methods             | String validation              |
| `zfill/center`              | String padding                 |
| `format`                    | String formatting              |

---

If you want me to:

* explain with internal memory model
* show all methods with sample input/output tables
* or provide practice problems for each

Let me know and I’ll continue in that direction.

"""