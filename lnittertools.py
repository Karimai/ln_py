import itertools

counter = itertools.count(start=5, step=-2.5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

mock_data = [10, 20, 30, 40, 50]
zipped_data = list(itertools.zip_longest(range(10), mock_data))
for data in zipped_data:
    print(data)  # default is None for short
i = 0
for c in itertools.cycle(mock_data):
    i += 1
    print(c)
    if i == 10:
        break  # itertools.cycle creates an infinite loop

switch = itertools.cycle(("On", "Off"))
print(next(switch))
print(next(switch))
print(next(switch))

#  itertools.repeat is necessary when a given function such as map needs two iterators.
squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))


#  itertools.starmap makes it easy
squares = itertools.starmap(pow, itertools.zip_longest([0, 1, 2, 3], [], fillvalue=2))
print(list(squares))

# Combinations: all the different ways you can group a certain number of items. Order does NOT matter
# (a, b) == (b, a), so they can not appear both at the same time.
# Permutation: A combination when order does matter
