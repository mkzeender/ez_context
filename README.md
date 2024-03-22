# EZ Context Managers

Allows you to create generator-based context managers without try-finally.
Fully statically-typed and thread safe.

Example:
```python
@context_mgr
def suppress_and_print():
    print("entering")
    error = yield
    print(error)
    return True  # suppress error


with suppress_and_print:
    raise Exception("Hello")
```