from collections import Counter
from dataclasses import dataclass
from typing import List
from collections import namedtuple

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


def named_tuples():
    Person = namedtuple('Person', ['name', 'age', 'gender'])
    karim = Person(name='Karim', age=41, gender='Male')
    ameneh = Person(name='Ameneh', age=45, gender='Female')

    print(karim)
    print(ameneh)

    karim = karim._replace(age=42)
    print(karim)


def test_named_tuples():
    named_tuples()
