def isPP(n):
    for m in range(2, (n ** 0.5) + 1):
        k = 2
        while m ** k <= n:
            if m ** k == n:
                return [m, k]
    return None


def test_isPP():
    assert isPP(4) == [2, 2]


def automorphic(n):
    return "Automorphic" if str(n * n).endswith(str(n)) else "Not!!"


def test_automorphic():
    assert automorphic(95) == "Not!!"


"""
My little sister came back home from school with the following task: given a squared sheet 
of paper she has to cut it in pieces which, when assembled, give squares the sides of which 
form an increasing sequence of numbers. At the beginning it was lot of fun but little by 
little we were tired of seeing the pile of torn paper. So we decided to write a program that 
could help us and protects trees.

Task
Given a positive integral number n, return a strictly increasing sequence (list/array/string 
depending on the language) of numbers, so that the sum of the squares is equal to n².

If there are multiple solutions (and there will be), return as far as possible the result with 
the largest possible values:

Examples
decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 
11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is 
smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] 
doesn't form a strictly increasing sequence.

"""


def decompose(n, remaining_sum=None):
    """
    The algorithm uses recursion and backtracking.
    :param n:
    :param remaining_sum:
    :return:
    """
    # This means we've successfully formed a sequence of squares that sum up to n squared,
    # and we return an empty list to indicate that the sequence is complete.
    if remaining_sum == 0:
        return []

    if remaining_sum is None:
        remaining_sum = n * n

    for current_num in range(min(n-1, int(remaining_sum ** 0.5)), 0, -1):
        sub_seq = decompose(current_num, remaining_sum - current_num ** 2)
        if sub_seq is not None:
            return sub_seq + [current_num]

    return None


def test_decompose():
    assert decompose(11) == [1, 2, 4, 10]


# 7      6     5      4     3     2     1  (digits of 1234567 from the right)
# ×      ×     ×      ×     ×     ×     ×  (multiplication)
# 1     10     9     12     3     4     1  (the repeating sequence)
# 9*1+2*10+5*9 +8*12 = 170
# 0*1+7*10+1*9 = 79
# 9*1+7*10 = 79
def thirt(n):
    # Define the fixed sequence for the transformation
    sequence = [1, 10, 9, 12, 3, 4]

    # Initialize variables for the previous and current sum
    prev_sum = -1
    current_sum = 0

    # Continue the loop until the sum stabilizes
    while prev_sum != current_sum:
        index = 0
        prev_sum = current_sum
        current_sum = 0

        # Calculate the new sum based on the sequence
        while n:
            digit = n % 10
            current_sum += digit * sequence[index]
            index = (index + 1) % 6
            n //= 10

        # Update the value of n for the next iteration
        n = current_sum

    return current_sum


def test_thirt():
    assert thirt(1234567) == 87
    assert thirt(8529) == 79
    assert thirt(85299258) == 31
    assert thirt(5634) == 57
    assert thirt(1111111111) == 71
    assert thirt(987654321) == 30


def disarium_number(number):
    dgs_sum = 0
    for i, d in enumerate(str(number)):
        dgs_sum += (int(d) ** (i+1))
    print(dgs_sum, number)
    return "Disarium !!" if dgs_sum == number else "Not !!"


def test_disarium_number():
    disarium_number(89)
