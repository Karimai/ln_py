from collections import OrderedDict

def ordered_items():
    items = [
        "BANANA FRIES 12",
        "POTATO CHIPS 30",
        "APPLE JUICE 10",
        "CANDY 5",
        "APPLE JUICE 10",
        "CANDY 5",
        "CANDY 5",
        "CANDY 5",
        "POTATO CHIPS 30",
    ]
    ordered_items = OrderedDict()
    for item in items:
        itm, price = item.rsplit(" ", 1)
        if itm in ordered_items:
            ordered_items[itm] += int(price)
        else:
            ordered_items[itm] = int(price)

    for item, price in ordered_items.items():
        print(item, price)


def test_ordered_items():
    ordered_items()
