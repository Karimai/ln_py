def sort_by_length(arr):
    return sorted(arr, key=lambda x: len(x))


def test_sort_by_length():
    assert sort_by_length(["beg", "life", "i", "to"]) == ["i", "to", "beg", "life"]
