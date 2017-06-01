A sandbox for simulating my usual work with Fortran using global
variables.

It seems that I could not use Python modules for declaring mutable global
variables (??).


```python
a = 33
def modify_a():
    a = 55

print(a)  # a will still be 33
```

Using module:

```python
from global_vars import a

def modify_a():
    a = 1.1
```



