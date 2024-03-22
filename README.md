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

# parentheses optional unless the func has arguments
with suppress_and_print: 
    raise Exception("Hello")
```

See examples.py for more examples.

Created for a comment on [this MCoding video](https://www.youtube.com/watch?v=LBJlGwJ899Y&t=36s)