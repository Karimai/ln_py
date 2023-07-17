from collections import defaultdict
from typing import List


def stock_list(list_of_art: List[str], list_of_cat: List[str]):
    book_shelves = defaultdict(lambda: 0)

    for item in list_of_art:
        items = item.split()
        book_shelves[item[0]] += int(items[-1])

    if not sum(p for p in book_shelves.values()): return ""

    return ' - '.join([f"({c} : {book_shelves[c]})" for c in list_of_cat])


def test_stock_list():
    b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B", "C", "D"]
    assert stock_list(b, c) == "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"
