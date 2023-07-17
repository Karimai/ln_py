import re


def simple_sample(data):
    return re.match("^[1-3]", str(data))


def test_simple_sample():
    print(simple_sample(1))
