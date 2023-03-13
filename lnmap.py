def square(number: int):
    return number * number


# It is a set and the repeated values will be removed automatically
numbers = {1, 2, 3, 4, 5, 4}

square_numbers = map(square, numbers)
# map return a generator and you have loop through it.
for num in square_numbers:
    print(num)
