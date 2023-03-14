class AClass:
    def __init__(self):
        self.name = 'Karim'
        self._name = 'Javad'
        self.__name = 'Masoud'

    def update_name(self, name):
        self.__name = name


a_class = AClass()

a_class.name = 'Charim'
a_class._name = 'Javaad'
a_class.__name = 'Rassol'  # It just adds another attribute.


print(a_class.__dict__)
# {'name': 'Charim',
# '_name': 'Javaad',
# '_AClass__name': 'Masoud',
# '__name': 'Rassol'}

a_class.update_name('Rasoul')
print(a_class.__dict__)
# 'name': 'Charim',
# '_name': 'Javaad',
# '_AClass__name': 'Rasoul',
# '__name': 'Rassol'}

xyz = 1,000,000
# x y z = 1000 2000 3000
x,y,z = 1000, 2000, 3000
x_y_z = 1,000,000

print(xyz)
print(x, y, z)
print(x_y_z)

x, *_, y = 1, 2, 3, 4, 7, 5, 6

print(x)
print(y)
print(_)
