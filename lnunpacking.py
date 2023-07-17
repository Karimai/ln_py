def multiply(*args):
    print(type(args))


def splat(**kwargs):
    for arg in kwargs.items():
        print(arg)


vars = [2, 3, 4]
multiply(*vars)

kwargs = {"Name": "Karim", "Age": 41}
splat(**kwargs)


def f(x, y, z):
    return x + y + z


print(f(*[1, 2, 3]))
print(f(**{"x": 1, "y": 2, "z": 3}))

# Extended unpacking
a, *b = [1, 2, 3, 4, 5]
print(a)
print(b)

# Merging two dictionaries
first = {"one": 1, "two": 2}
second = {"third": 3}
together = {**first, **second}
print(together)
