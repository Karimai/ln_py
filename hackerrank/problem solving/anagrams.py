from typing import List
from itertools import permutations


def generate_anagrams(word):
    anagrams = set()
    for p in permutations(word):
        anagrams.add(''.join(p))
    return anagrams


def stringAnagram(dictionary: List[str], query: List[str]):
    res = []
    for qry in query:
        anagrams = set(generate_anagrams(qry))
        for i, an in enumerate(anagrams):
            if an in dictionary:
                print(an)
        res.append(sum(1 for anagram in anagrams if anagram in dictionary))
    print(res)
    return res


def test_stringAnagram():
    assert stringAnagram(['heater', 'cold', 'clod', 'reheat', 'docl'], ['codl', 'heater', 'abcd']) == [3, 2, 0]

# input_word = "python"
# anagrams_set = generate_anagrams(input_word)
# print(anagrams_set)
