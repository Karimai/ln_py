def round_to_next5(n):
    if n >= 0:
        return sum([(n // 5) * 5, (n % 5 > 0) * 5])
    if not n % 5:
        return n
    res = abs(n) % 5
    return -n + 5


def test_round_to_next5():
    assert round_to_next5(0) == 0
    assert round_to_next5(2) == 5
    assert round_to_next5(5) == 5
    assert round_to_next5(-2) == 0


def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5: return "Underweight"
    if bmi <= 25.0: return "Normal"
    if bmi <= 30.0: return "Overweight"
    return "Obese"


def test_bmi():
    # assert bmi(50, 1.80) == "Underweight"
    assert bmi(80, 1.80) == "Normal"


def twice_as_old(dad, son):
    return abs(dad - 2 * son)
    # for i in range(son, 0, -1):
    #     print(i)
    #     if (dad - i) == (son - i) * 2: return i
    # for i in range(200):
    #     double_dad = (dad + i)
    #     double_son = ((son + i) * 2)
    #     if (dad + i) == (son + i) * 2: return i
    # return 0


def test_twice_as_old():
    assert twice_as_old(28, 10) == 8
