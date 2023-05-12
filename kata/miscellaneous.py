"""
Task
You will be given an array of numbers.
You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

"""
from typing import List


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
