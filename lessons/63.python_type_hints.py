"""
### 🧠 What Are Python Type Hints?

**Python type hints** (also called **type annotations**) are a feature introduced in **Python 3.5** (and greatly enhanced in 3.9+) that allow you to **explicitly declare the data types** of variables, function arguments, and return values.

> ⚠️ They **do not enforce types at runtime**, but they **help developers, IDEs, and tools (like FastAPI or mypy)** understand and check your code better.

---

### ✅ Why Use Type Hints?

| Benefit                   | Description                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------- |
| ✔️ **Readability**        | Makes code easier to understand by showing what types are expected                                        |
| ✔️ **Editor support**     | Better **autocomplete**, **inline documentation**, and **static analysis** in IDEs like VSCode or PyCharm |
| ✔️ **Fewer bugs**         | Tools like `mypy`, `pyright`, or `pylint` can catch type mismatches **before runtime**                    |
| ✔️ **Helps frameworks**   | FastAPI, Pydantic, PyDanticV2 use them to do **automatic validation** and **doc generation**              |
| ✔️ **Code documentation** | Functions become almost self-documenting                                                                  |

---

### 📌 Basic Syntax

```python
def greet(name: str) -> str:
    return "Hello " + name
```

Here:

* `name: str` means `name` must be a string.
* `-> str` means the function will return a string.

---

### 📦 Common Built-in Type Hints

| Type                | Syntax                                 |        |
| ------------------- | -------------------------------------- | ------ |
| Integer             | `int`                                  |        |
| Float               | `float`                                |        |
| String              | `str`                                  |        |
| Boolean             | `bool`                                 |        |
| List                | `list[int]` or `List[int]`             |        |
| Dictionary          | `dict[str, int]` or `Dict[str, int]`   |        |
| Tuple               | `tuple[int, str]` or `Tuple[int, str]` |        |
| Optional (nullable) | `Optional[str]` or \`str               | None\` |
| Any type            | `Any`                                  |        |
| Callable            | `Callable[[int, int], int]`            |        |

> From Python 3.9+, you can use built-in generics like `list[int]` instead of `List[int]` (from `typing`).

---

### 📘 Examples

#### Function Parameters and Return Types

```python
def add(a: int, b: int) -> int:
    return a + b
```

#### Variables

```python
x: float = 3.14
name: str = "Kedar"
active: bool = True
```

#### List and Dictionary

```python
from typing import List, Dict

students: List[str] = ["Alice", "Bob", "Charlie"]
marks: Dict[str, int] = {"Alice": 85, "Bob": 90}
```

#### Optional Type

```python
from typing import Optional

def find_user(id: int) -> Optional[str]:
    if id == 1:
        return "Kedar"
    return None
```

#### Using `Any`

```python
from typing import Any

def process(data: Any) -> None:
    print(data)
```

---

### 🧪 Tools That Use Type Hints

| Tool/Framework | How it uses type hints                                  |
| -------------- | ------------------------------------------------------- |
| **mypy**       | Static type checker                                     |
| **pyright**    | Fast type checker (used in VSCode)                      |
| **FastAPI**    | Auto-generates request validation and docs              |
| **Pydantic**   | Uses type hints to validate data models                 |
| **IDEs**       | Improve autocompletion, detect bugs before running code |

---

### ⚠️ Limitations

* **No enforcement at runtime** (unless you use external tools).
* Complex type hints can be hard to read (`Callable`, `Union`, `TypedDict`, etc.).
* Doesn’t eliminate the need for runtime checks in mission-critical code.

---

### 💡 Real-World Example (FastAPI)

```python
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/user")
def create_user(user: User) -> dict:
    return {"message": f"User {user.name} created."}
```

Here:

* `user: User` tells FastAPI to expect a JSON object with `name:str` and `age:int`.
* FastAPI uses type hints to **automatically validate and document** this.

---

Let me know if you want to dive into **advanced type hints** like `Union`, `Literal`, `TypedDict`, `TypeVar`, or **runtime type checking** tools like `pydantic`, `beartype`, or `enforce`.

"""
