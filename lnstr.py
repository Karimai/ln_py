"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )


"""
import string
from typing import List


def alphabet_position(alphas):
    return " ".join(
        str(string.ascii_lowercase.index(ch) + 1)
        for ch in alphas.lower()
        if ch in string.ascii_lowercase
    )


def test_alphas_replace():
    assert (
        alphabet_position("The sunset sets at twelve o' clock.")
        == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    )


"""
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).

Examples
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
"""


def count_by(n, x):
    return [n * i for i in range(1, x + 1)]


def test_count_by():
    assert count_by(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert count_by(2, 5) == [2, 4, 6, 8, 10]


"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


def solution(s: str):
    return "".join(ch if ch in string.ascii_lowercase else " " + ch.upper() for ch in s)


def test_solution():
    assert solution("helloWorld") == "hello World"


"""
This function should test if the factor is a factor of base.

Return true if it is a factor or false if it is not.

About factors
Factors are numbers you can multiply together to get another number.

2 and 3 are factors of 6 because: 2 * 3 = 6

You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
You can use the mod operator (%) in most languages to check for a remainder
For example 2 is not a factor of 7 because: 7 % 2 = 1

Note: base is a non-negative number, factor is a positive number.
"""


def check_for_factor(base, factor):
    return base % factor == 0


def test_check_for_factor():
    assert check_for_factor(6, 2) is True


""" This code is way too easy compared to the process of finding it, so here is the explanation:

1) First we establish that h(n, m) = 1 + h(n, m-1) + h(n-1, m-1) by reasoning on the outcomes of an egg drop at a given floor f:
   - if it breaks, we have n-1 eggs and m-1 tries left, and we know the target floor is at most f-1, so to be guaranteed to find
     the target floor, f-1 <= h(n-1, m-1).
   - otherwise, we have n eggs and m-1 tries left, and we know the target floor is at least f+1, so to be guaranteed to find the
     target floor, h(n, m) - f <= h(n, m-1)
   This allows us to implement a naive dynamic programming approach, or a square and multiply approach with the corresponding
   matrix (good for small n and big m), but both are unfortunately too costly to pass the tests.

2) Then comes the hard part (at least for me, maybe there's a simpler way): realizing that h(n, m) is actually the sum of
   Pascal's triangle m first rows truncated at n first elements (a.k.a. n first columns truncated at row m).
   One way to see that is to start recursively expanding h(n,m): (abbreviated notation hij = h(n-i, m-j))

   h00 = 1[00] + h01 + h11
       = 1[00] + (1[01] + h02 + h12) + (1[11] + h12 + h22)
       = 1[00] + 1[01] + 1[11] + h02 + 2*h12 + h22
       = 1[00] + 1[01] + 1[11] + (1[02] + h03 + h13) + 2*(1[12] + h13 + h23) + (1[22] + h23 + h33)
       = 1[00] + 1[01] + 1[11] + 1[02] + 2[12] + 1[22] + h03 + 3*h13 + 3*h23 + h33
       = 1[00] +
         1[01] + 1[11] +
         1[02] + 2[12] + 1[22] +
         1[03] + 3[13] + 3[23] + 1[33] + ...

3) Finally, we can use the fact that the sum of a column k of Pascal's triangle (k,k) + (k+1,k) + ... + (m,k) is equal to
   (m+1,k+1), so we only need to compute the sum of the 2nd to n+1st element of row m+1.
"""


def height(n, m):
    if n == 0 or m == 0:
        return 0
    if n >= m:
        return 2**m - 1

    res = 0
    pascalNum = 1
    for i in range(1, n + 1):
        pascalNum = pascalNum * (m + 1 - i) // i
        res += pascalNum

    return res


def test_height():
    assert height(2, 14) == 105


"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""


def solution(text: str, ending: str):
    return text.endswith(ending)


"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""


def descending_order(num):
    num_str = str(num)
    num_str.sort()


def validate_pin(pin):
    for d in pin:
        if d not in string.digits:
            return False
    return len(pin) in [4, 6]


def test_validate_pin():
    assert validate_pin("123") is False


from functools import reduce


def grow(arr):
    return reduce(lambda x, y: x * y, arr)


def test_grow():
    assert grow([1, 2, 3]) == 6


def divisors(n):
    count = 1
    for i in range(2, n + 1):
        if n % i == 0:
            count += 1
    return count


def test_divisors():
    assert divisors(1) == 1
    assert divisors(4) == 3


def two_sum(numbers, target):
    for i, val_i in enumerate(numbers):
        expected = target - val_i
        if expected in numbers[i + 1 :]:
            return [i, numbers[i + 1 :].index(expected) + i + 1]


def test_two_sum():
    assert two_sum([1, 2, 3], 4) == [0, 2]
    assert two_sum([2, 2, 3], 4) == [0, 1]
    assert two_sum([1234, 5678, 9012], 14690) == [1, 2]


ad = (
    "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,"
    "54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,"
    "10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000,"
    "22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45521,10 Surta Alley Goodtown GG 30654,"
    "45 Holy Grail Al. Niagara Town ZP 32908,320 Main Al. Bern AE 56210,14 Gordon Park Atlanta RE 13000,"
    "100 Pussy Cat Rd. Chicago EX 34342,2 Gordon St. Atlanta RE 13000,5 Gordon Road Atlanta RE 13000,"
    "2200 Tokyo Av. Tedmondville SW 43098,67 Paris St. Abbeville AA 45521,11 Surta Avenue Goodtown GG 30654,"
    "45 Holy Grail Al. Niagara Town ZP 32918,320 Main Al. Bern AE 56215,14 Gordon Park Atlanta RE 13200,"
    "100 Pussy Cat Rd. Chicago EX 34345,2 Gordon St. Atlanta RE 13222,5 Gordon Road Atlanta RE 13001,"
    "2200 Tokyo Av. Tedmondville SW 43198,67 Paris St. Abbeville AA 45522,11 Surta Avenue Goodville GG 30655,"
    "2222 Tokyo Av. Tedmondville SW 43198,670 Paris St. Abbeville AA 45522,114 Surta Avenue Goodville GG 30655,"
    "2 Holy Grail Street Niagara Town ZP 32908,3 Main Rd. Bern AE 56210,77 Gordon St. Atlanta RE 13000"
)


code = (
    "OH 43071,NY 56432,ZP 32908,AE 56210,RE 13000,EX 34342,SW 43098,AA 45521,GG 30654,ZP 32908,AE 56215,RE 13200,EX 34345,"
    "RE 13222,RE 13001,SW 43198,AA 45522,GG 30655,XX 32321,YY 45098"
)


def travel(r, zipcode):
    if not zipcode:
        return ":/"
    addresses = r.split(",")
    codes = []
    cities = []
    for address in addresses:
        if address.endswith(zipcode):
            code, city = address.split(" ", 1)
            codes.append(code.strip())
            cities.append(city[: -len(zipcode)].strip())
    return f"{zipcode}:" + ",".join(cities) + "/" + ",".join(codes)


def test_travel():
    # assert travel(ad, "AA 45522") == "AA 45522:Paris St. Abbeville,Paris St. Abbeville/67,670"
    # assert travel(ad, "EX 34342") == "EX 34342:Pussy Cat Rd. Chicago,Pussy Cat Rd. Chicago/10,100"
    # assert travel(ad, "EX 34345") == "EX 34345:Pussy Cat Rd. Chicago/100"
    # assert travel(ad, "AA 45521") == "AA 45521:Paris bd. Abbeville,Paris St. Abbeville/674,67"
    # assert travel(ad, "AE 56215") == "AE 56215:Main Al. Bern/320"
    assert travel(ad, "") == ":/"


def find_it(seq):
    set_seq = list(set(seq))
    for num in set_seq:
        if seq.count(num) % 2 != 0:
            return num
    return 0


def test_find_it():
    assert find_it([7]) == 7
    assert find_it([1, 1, 7]) == 7


def dirReduc(arr):
    opposites = {"NORTH": "SOUTH", "WEST": "EAST", "SOUTH": "NORTH", "EAST": "WEST"}
    path = []
    for dir in arr:
        if len(path) == 0:
            path.append(dir)
        elif path[-1] == opposites[dir]:
            path.pop()
        else:
            path.append(dir)
    return path


def test_dir_reduc():
    assert dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) == [
        "WEST"
    ]
    assert dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]) == [
        "NORTH",
        "WEST",
        "SOUTH",
        "EAST",
    ]


def sum_two_smallest_numbers(numbers: List[int]):
    numbers.sort()
    return sum(numbers[0:2])


def test_sum_two_smallest_numbers():
    assert sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13
    assert sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19
    assert sum_two_smallest_numbers([25, 42, 12, 18, 22]) == 30
