import gc
import os
import time

import psutil
import requests

cars = []


class Memory:
    symbols = []

    def __init__(self, sym):
        self.symbols.append(sym)

    def get_symbol(self):
        return self.symbols


print(len(gc.get_objects()))
mem = Memory(1)
del mem

mem2 = Memory(2)

for i in range(100):
    Memory(i)

gc.collect()
print(len(gc.get_objects()))
print(mem2.get_symbol())
