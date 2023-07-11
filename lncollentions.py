from collections import Counter
from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    name: str
    rank: int


if __name__ == "__main__":
    names = ['Bart', "Karim", "Ali", "Abo", "John", "Jace"]
    ranks = [1, 3, 2, 1, 1, 2]
    people: List[Item] = []
    for person in zip(names, ranks):
        people.append(Item(name=person[0], rank=person[1]))

    print(people)

    people_dic = Counter(people)
