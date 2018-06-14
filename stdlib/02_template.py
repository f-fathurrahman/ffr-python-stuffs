import string

values = {"var": "foo"}

# Using template
t = string.Template("""
Variable         : $var
Escape           : $$
Variable in text : ${var}iable
""")

print("TEMPLATE: ", t.substitute(values))

# Using string interpolation
s = """
Variable         : %(var)s
Escape           : %%
Variable in text : $(var)siable
"""

print("INTERPOLATION: ", s % values)

# Using format
s = """
Variable : {var}
Escape : {{}}
Variable in text : {var}iable
"""

print("FORMAT: ", s.format(**values))

