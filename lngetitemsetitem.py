class Text:
    def __init__(self, names: str):
        self.names = names.split(" ")

    def __getitem__(self, item):
        print(self.names.index(item))
        return self.names.index(item)

    def __setitem__(self, key, value):
        while len(self.names) <= key - 1:
            self.names.append("temp")
        self.names.append(value)
        print(key, ":\t ", value)


my_text = Text("Karim Javad Rasoul")
javad = my_text["Rasoul"]
my_text[4] = "Ali"
print(my_text.names)
