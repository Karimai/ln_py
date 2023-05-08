def multiply(*args):
    print(type(args))


def splat(**kwargs):
    for arg in kwargs.items():
        print(arg)


vars = [2, 3, 4]
multiply(*vars)

kwargs = {"Name": "Karim", "Age": 41}
splat(**kwargs)
