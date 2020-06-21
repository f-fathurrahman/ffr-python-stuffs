Python 3 string formatting

Formatting with leading zeros:
```python
for i in range(100):
    filename = "IMG_{:04d}".format(i)
    print(filename)
```

# Modules to explore

itertools

shutil


# Installing packages

```
python setup.py build
python setup.py install
```