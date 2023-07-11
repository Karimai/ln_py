"""
Task
You will be given an array of numbers.
You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

"""
import copy
import time
from dataclasses import dataclass
from functools import cache, reduce, total_ordering
from string import ascii_lowercase
from typing import ClassVar, List


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
    if len(test) != len(original):
        return False
    for ch in test.lower():
        original = original.lower().replace(ch, "", 1)
    return original == ""


def test_is_anagram():
    assert is_anagram("foefet", "toffee") is True
    assert is_anagram("dumble", "bumble") is False
    assert is_anagram("apple", "pale") is False


def for_else(num: int):
    nums = [1, 2, 3, 4, 5, 6]
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


@cache
def ex_func(num):
    st = time.perf_counter()
    print("computing ... ", st)
    time.sleep(1)
    return round(time.perf_counter() - st)


def test_ex_func():
    assert ex_func(3) == 1
    assert ex_func(3) == 0


if __name__ == "__main__":
    ex_func(3)


def find_multiples(integer, limit):
    res = [integer]
    i = 2
    while True:
        if limit < i * integer:
            break
        res.append(i * integer)
        i += 1
    return res


def test_find_multiples():
    assert find_multiples(5, 25) == [5, 10, 15, 20, 25]


"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters 
and numeric digits that occur more than once in the input string. The input string can be assumed 
to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""


def duplicate_count(text):
    text = text.lower()
    from string import ascii_letters, digits
    ch_counter = {}
    for ch in ascii_letters + digits:
        if text.count(ch) >= 2:
            ch_counter[ch] = text.count(ch)
    print(len(ch_counter))
    return len(ch_counter)


def test_dublicate_count():
    assert duplicate_count("abcdeaB") == 2


"""
You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. 
Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

Example:
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13
"""


def mxdiflg(a1, a2):
    if not a1 or not a2: return -1
    min_a1, max_a1 = len(min(a1, key=len)), len(max(a1, key=len))
    min_a2, max_a2 = len(min(a2, key=len)), len(max(a2, key=len))
    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))


def test_mxdiflg():
    a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
    a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
    assert mxdiflg(a1, a2) == 13


"""
Kata Task
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
"""


def human_years_cat_years_dog_years(human_years):
    cat_years = dog_years = 15
    for years in range(2, human_years + 1):
        if years == 2:
            cat_years = dog_years = 24
        else:
            cat_years += 4
            dog_years += 5
    return [human_years, cat_years, dog_years]


def test_human_years_cat_years_dog_years():
    assert human_years_cat_years_dog_years(1) == [1, 15, 15]
    assert human_years_cat_years_dog_years(2) == [2, 24, 24]
    assert human_years_cat_years_dog_years(10) == [10, 56, 64]


def test_list_typing():
    from typing import List

    lst: List[str] = []
    print(len(lst))


# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python


@dataclass
class Item:
    first_str: ClassVar[str]
    second_str: ClassVar[str]
    ch: str
    repeat: int
    belong: str

    def __lt__(self, other):
        if self.repeat < other.repeat:
            return True
        if other.repeat < self.repeat:
            return False

        if self.belong == other.belong:
            return self.ch > other.ch
        if self.belong == '=' or other.belong == '=':
            return self.belong > other.belong
        return self.belong > other.belong


def mix(s1: str, s2: str):
    items: List[Item] = []
    Item.first_str = copy.deepcopy(s1)
    Item.second_str = copy.deepcopy(s2)
    processed_chs = ""
    for ch in s1.replace(' ', '') + s2.replace(' ', ''):
        if ch.isupper() or ch in processed_chs:
            continue
        processed_chs += ch
        ch_in_s1 = s1.count(ch)
        ch_in_s2 = s2.count(ch)
        if max(ch_in_s1, ch_in_s2) <= 1:
            continue
        if ch_in_s1 > ch_in_s2:
            items.append(Item(ch, ch_in_s1, "1"))
        elif ch_in_s1 < ch_in_s2:
            items.append(Item(ch, ch_in_s2, "2"))
        else:
            items.append(Item(ch, ch_in_s1, "="))

    sorted_items = sorted(items, reverse=True)
    res: List[str] = []
    for item in sorted_items:
        res.append(str(item.belong) + ":" + item.ch * item.repeat)
    return "/".join(res)


def test_mix():
    assert mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr"
    assert mix("Sadus:cpms>orqn3zecwGvnznSgacs",
               "MynwdKizfd$lvse+gnbaGydxyXzayp") == '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'
    assert mix("looping is fun but dangerous",
               "less dangerous than coding") == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
    assert mix(" In many languages",
               " there's a pair of functions") == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
    assert mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo"
    assert mix("codewars", "codewars") == ""
    assert mix("A generation must confront the looming ",
               "codewarrs") == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"

