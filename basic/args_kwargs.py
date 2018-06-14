def func1(*args):
    for a in args:
        print(a)

def func2(**kwargs):
    for a in kwargs:
        print(a, " ", kwargs[a])

func1(1,3,4)

func2(name="efefer",age=30)
