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


def hackerrank_list():
    lst = []
    cmds = ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1", "sort", "print", "pop", "reverse", "print"]
    for cmd in cmds:
        current_cmd, *args = cmd.split()
        if current_cmd == "insert":
            lst.insert(int(args[0]), int(args[1]))
        elif current_cmd == "print":
            print(lst)
        elif current_cmd == "remove":
            lst.remove(int(args[0]))
        elif current_cmd == "append":
            lst.append(int(args[0]))
        elif current_cmd == "sort":
            lst.sort()
        elif current_cmd == "pop":
            lst.pop()
        else:
            lst = lst[::-1]


def test_hackerrank_list():
    hackerrank_list()


def prod_sum():
    N, M = 4, 2
    mat = []
    inputs = ["2 5", "3 7", "1 3", "4 0"]
    for r in range(N):
        row = list(map(int, inputs[r].split()))
        mat.append(row)

    total_row = [sum(row[i] for row in mat) for i in range(M)]
    from functools import reduce
    print(reduce(lambda x, y: x * y, total_row))

    min_ax = []
    min_ax = [min(row) for row in mat]

    min_axis_1 = [min(num for num in row for row in mat)]
    print(max(min_axis_1))


def test_prod_sum():
    prod_sum()


"""
Find the sum of the odd numbers within an array, after cubing the initial integers.
The function should return None if any of the values aren't numbers.

Note: Booleans should not be considered as numbers.
"""


def cube_odd(numbers: List):
    if not all(type(num) is int for num in numbers):
        return None
    odds = [num for num in numbers if num % 2]
    return sum(num ** 3 for num in odds)


def test_cube_odd():
    assert cube_odd([True, 12]) is None
    assert cube_odd([1, 2, 3, 4]) == 28


"""
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.
"""


def up_array(arr: List[int]):
    len_input = len(arr)
    if not all(type(num) == int and 0 <= num <= 9 for num in arr):
        return None
    num = int(''.join(str(a) for a in arr))
    len_result = len([int(ch) for ch in str(int(num) + 1)])
    needed_zeros = len_input - len_result
    return [0] * needed_zeros + [int(ch) for ch in str(int(num) + 1)]


def test_up_array():
    assert up_array([0, 4, 2]) == [0, 4, 3]


def max_sequence(arr):
    if not arr or all(num < 0 for num in arr):
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example usage
def test_max_sequence():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_sequence(arr)
    print(result)  # Output: 6


def ordered_count(inp):
    inp_set = set(inp)
    res = []
    for ch in inp:
        if ch in inp_set:
            res.append((ch, inp.count(ch)), )
            inp_set.discard(ch)
    return res


def test_ordered_count():
    res = ordered_count('abracadabra')
    print(res)
