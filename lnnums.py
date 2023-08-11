def even_numbers(arr, number):
    even_nums = []
    for i in arr[::-1]:
        if not i % 2:
            even_nums.insert(0, i)
            if len(even_nums) == number:
                return even_nums
    ev_nums = [i for i in arr[::-1] if not i % 2]
    return []


def test_even_numbers():
    assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [4, 6, 8]

