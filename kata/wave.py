"""
In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.
"""


def wave(people):
    # Code here
    # wave = []
    # for i, ch in enumerate(people):
    #     wave.append(people[:i] + ch.upper() + people[i+1:])
    # return wave
    return [people[:i] + ch.upper() + people[i+1:] for i, ch in enumerate(people) if not ch.isspace()]


def test_wave():
    # assert wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    assert wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]


