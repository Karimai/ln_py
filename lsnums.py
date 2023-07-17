from functools import reduce
from operator import mul


def number_to_pwr(num, p):
    nums = [num for _ in range(p)]
    return reduce(mul, nums)


def test_number_to_pwr():
    assert number_to_pwr(3, 2) == 9
