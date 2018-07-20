from jinja2 import Template

def my_func1():
    return "This is called from my_func1"

def my_func2():
    print("This is from my_func2")

def my_func3():
    print("This is done")
    return 3*2.1
# function with no argument
t = Template("{{ fnc() }}")

print( t.render( fnc=lambda: 10 ) )

print( t.render( fnc=my_func1 ) )  # without ()

print( t.render( fnc=my_func2 ) )  # without ()
# my_func2 will be executed and returned None

print( t.render( fnc=my_func3 ) )

# function with an argument
t = Template("{{ fnc(x) }}")

print( t.render( fnc=lambda v: v, x = "20" ) )
print( t.render( fnc=lambda v: v*3.2, x = 21 ) )

# function with default argument
t = Template("{{ fnc(v=31) }}")
print( t.render( fnc=lambda v: 2*v ) )  # function must use `v` as argument




