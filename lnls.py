from collections import defaultdict
from functools import reduce
from typing import List


def stock_list(list_of_art: List[str], list_of_cat: List[str]):
    book_shelves = defaultdict(lambda: 0)

    for item in list_of_art:
        items = item.split()
        book_shelves[item[0]] += int(items[-1])

    if not sum(p for p in book_shelves.values()): return ""

    return ' - '.join([f"({c} : {book_shelves[c]})" for c in list_of_cat])


def test_stock_list():
    b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B", "C", "D"]
    assert stock_list(b, c) == "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"


"""
Your task is to sum the differences between consecutive pairs in the array in descending order.

Example
[2, 1, 10]  -->  9
If the array is empty or the array has only one element the result should be 0.

"""


def sum_of_differences(arr: List[int]):
    if len(arr) < 2: return 0
    arr.sort(reverse=True)
    diffs = [arr[i] - arr[i+1] for i in range(len(arr) - 1)]
    return reduce(lambda x, y: x + y, diffs)


def test_sum_of_differences():
    assert sum_of_differences([1, 2, 10]) == 9


"""
https://www.codewars.com/kata/56f3a1e899b386da78000732/train/python
Write a function partlist that gives all the ways to divide a list (an array) of at least two elements into two 
non-empty parts.

Each two non empty parts will be in a pair (or an array for languages without tuples or a structin C - C: see Examples 
test Cases - )
Each part will be in a string
Elements of a pair must be in the same order as in the original array.
"""


def partlist(words: List[str]):
    # res = []
    # for i in range(1, len(words)):
    #     res.append((" ".join(words[:i]), " ".join(words[i:])))
    # return res
    return [(" ".join(words[:i]), " ".join(words[i:])) for i in range(1, len(words))]


def test_partlist():
    assert  partlist(["I", "wish", "I", "hadn't", "come"]) == [("I", "wish I hadn't come"),
                                                               ("I wish", "I hadn't come"),
                                                               ("I wish I", "hadn't come"),
                                                               ("I wish I hadn't", "come")]
    assert  partlist(["cdIw", "tzIy", "xDu", "rThG"]) == [("cdIw", "tzIy xDu rThG"),
                                                          ("cdIw tzIy", "xDu rThG"),
                                                          ("cdIw tzIy xDu", "rThG")]
    assert partlist(["vJQ", "anj", "mQDq", "sOZ"]) == [("vJQ", "anj mQDq sOZ"),
                                                        ("vJQ anj", "mQDq sOZ"),
                                                        ("vJQ anj mQDq", "sOZ")]
