from os import listdir
from os.path import isfile, join

print([f for f in listdir(".") if isfile(join(".", f))])
