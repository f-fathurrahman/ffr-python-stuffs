from __future__ import print_function

from jinja2 import Template

t = Template("{{ variable }}")

# Using built-in types

print( t.render(variable="This is a string") )

print( t.render(variable=100) )


# Using custom classes instances

class MyClass(object):
    
    def __str__(self):
        return "__str__"
    
    def __repr__(self):
        return "__repr__"

print( t.render( variable=MyClass() ) )



