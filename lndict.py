from collections import defaultdict


def count(s: str):
    res = defaultdict(lambda: 0)
    for c in s:
        res[c] += 1
    return res
    # return {c: s.count(c) for c in s}
