def isPP(n):
    for m in range(2, (n ** 0.5) + 1):
        k = 2
        while m ** k <= n:
            if m ** k == n:
                return [m, k]
    return None


def test_isPP():
    assert isPP(4) == [2, 2]
