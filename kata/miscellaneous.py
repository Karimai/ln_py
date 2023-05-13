"""
Task
You will be given an array of numbers.
You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

"""
from typing import List
from functools import reduce

def sort_array(source_array: List[int]):
    odds = [i for i in source_array if (i % 2)]
    # for i in source_array:
    #     if i % 2:
    #         odds.append(i)
    odds.sort()
    ret = [odds.pop(0) if val % 2 else val for i, val in enumerate(source_array)]
    # for i, val in enumerate(source_array):
    #     if val % 2:
    #         source_array[i] = odds.pop(0)
    return ret


def test_sort_array():
    assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]



"""
In this simple exercise, you will create a program that will take two lists of integers, a and b.
Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b.
You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and
the volume of b is 20. Therefore, the function should return 8.
"""


def find_difference(a, b):
    vol_a = reduce(lambda x, y: x * y, a)
    vol_b = reduce(lambda x, y: x * y, b)
    return abs(vol_b - vol_a)


def test_find_difference():
    assert find_difference([3, 2, 5], [1, 4, 4]) == 14

