def is_anagram(a: str, b: str):
    return set(a.lower()) == set(b.lower())


def test_is_anagram():
    assert is_anagram("Ali", "Lia") is True
    assert is_anagram("Ball", "bill") is False
