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
a_class.__name = 'Rassol'

print(a_class.__dict__)
# {'name': 'Charim',
# '_name': 'Javaad',
# '_AClass__name': 'Masoud',
# '__name': 'Rassol'}  NOTE: You just added another attribute here

a_class.update_name('Rasoul')
print(a_class.__dict__)
# 'name': 'Charim',
# '_name': 'Javaad',
# '_AClass__name': 'Rasoul',
# '__name': 'Rassol'}
