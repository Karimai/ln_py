from collections import defaultdict, Counter
from typing import List


def count(s: str):
    res = defaultdict(lambda: 0)
    for c in s:
        res[c] += 1
    return res
    # return {c: s.count(c) for c in s}


def important_chars(name: str):
    chars = defaultdict(int)
    for ch in name:
        chars[ch] += 1
    sorted_chars = sorted(chars.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_chars)
    return sorted_chars


def test_important_chars():
    assert important_chars("Google") == [('o', 2), ('G', 1), ('e', 1), ('g', 1), ('l', 1)]


"""
Complete the method which returns the number which is most frequent in the given input array.
If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.
"""


def highest_rank(numbers: List):
    counter = Counter(numbers)
    max_count = max(counter.values())
    return max(k for k, v in counter.items() if v == max_count)


def test_highest_rank():
    assert highest_rank([12, 1, 2, 3, 2, 12]) == 12

