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


"""
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other;
return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"
"""

# write the function is_anagram


def is_anagram(test: str, original: str):
    if len(test) != len(original): return False
    for ch in test.lower():
        original = original.lower().replace(ch, "", 1)
    return original == ""


def test_is_anagram():
    assert is_anagram("foefet", "toffee") is True
    assert is_anagram("dumble", "bumble") is False
    assert is_anagram("apple", "pale") is False


def for_else(num: int):
    nums = [1, 2, 3, 4, 5, 6]
    res = ""
    for i in nums:
        if num == i:
            res = "Found!"
            break
    else:
        res = "Not found!"
    return res


def test_for_else():
    assert for_else(5) == "Found!"
    assert for_else(10) == "Not found!"
