from itertools import product
from typing import List


def simple_product():
    a = [1, 50]
    b = [2, 200]
    for x, y in product(a, b):
        print(x, y)


def is_even(num: int):
    return not num % 2


def get_even_numbers(nums: List[int]):
    return list(filter(is_even, nums))


def test_get_even_numbers():
    assert get_even_numbers([2,4,5,6]) == [2,4,6]


if __name__ == "__main__":
    simple_product()


def vert_mirror(strng: str):
    ls_strs = strng.split("\n")
    return "\n".join([s[::-1] for s in ls_strs])


def hor_mirror(strng: str):
    ls_strs = strng.split("\n")
    return "\n".join(s for s in ls_strs[::-1])


def oper(fct, s):
    return fct(s)


def test_vert_mirror():
    assert vert_mirror("abcd\nefgh\nijkl\nmnop") == "dcba\nhgfe\nlkji\nponm"


def test_hor_mirror():
    assert hor_mirror("abcd\nefgh\nijkl\nmnop") == "mnop\nijkl\nefgh\nabcd"


def test_oper():
    oper(hor_mirror, "abcd\nefgh\nijkl\nmnop") == "mnop\nijkl\nefgh\nabcd"
