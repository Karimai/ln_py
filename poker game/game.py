"""
https://www.codewars.com/kata/524c74f855025e2495000262/train/python
"""

import re

CardRank = ["", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


def hand(hole_cards, community_cards):
    validation = [True] * 5
    init_lst = [False] * 13
    pattern = r"^\d{1,2}|[AJQK]"
    rank_suit = []
    from collections import defaultdict

    counter = defaultdict(int)
    for card in hole_cards + community_cards:
        re_match = re.search(pattern, card)
        rank = re_match.group(0)
        suit = card.replace(rank, "")
        idx = CardRank.index(rank)
        rank_suit.append(
            (idx, suit),
        )
        init_lst[idx - 1] = True
        counter[rank] += 1

    for i in range(12, 3, -1):
        if all(init_lst[i - j] * validation[j] for j in range(5)):
            ranks = []
            for t in range(5):
                ranks.append(CardRank[i - t + 1])

            def get_suit(rr):
                sts = []
                for rk, st in rank_suit:
                    if CardRank.index(rr) == rk:
                        sts.append(st)
                return sts

            for s in "♠♦♥♣":
                f = 0
                for r in ranks:
                    if s in get_suit(r):
                        f += 1
                if f == 5:
                    return "straight-flush", ranks
    """
    Flush (five cards of the same suit). Higher ranks are better, compared from high to low rank.
    """
    for i in range(12, 4, -1):
        for s in "♠♦♥♣":
            if sum(1 for x in rank_suit if x[1] == s) >= 5:
                flush = "flush"
                ranks = []
                for rank, suit in rank_suit:
                    if suit == s:
                        ranks.append(rank)
                ranks.sort(reverse=True)
                caranks = []
                for ra in ranks:
                    caranks.append(CardRank[ra])
                return flush, caranks[:5]

    """
    Straight (five consecutive ranks). Higher rank is better.
    """
    for i in range(12, 3, -1):
        if all(init_lst[i - j] * validation[j] for j in range(5)):
            ranks = []
            for t in range(5):
                ranks.append(CardRank[i - t + 1])
            return "straight", ranks

    for i in range(12, 4, -1):
        for key, value in counter.items():
            if value >= 4:
                four_of_a_kind = "four-of-a-kind"
                ranks = []
                for r, _ in rank_suit:
                    if CardRank[r] != key:
                        ranks.append(r)
                ranks = list(set(ranks))
                ranks.sort(reverse=True)
                caranks = []
                for ra in ranks:
                    caranks.append(CardRank[ra])
                return four_of_a_kind, [key] + [caranks[0]]

    """
    Full house (three cards with the same rank, two with another).
    Tiebreaker is first the rank of the three cards, then rank of the pair.
    """
    for i in range(12, 4, -1):
        ranks = []
        needed = [2, 3]
        for key, value in counter.items():
            if value in needed:
                ranks.append(
                    (key, value),
                )
                needed.remove(value)
        if len(ranks) == 2:
            full_house = "full house"
            sorted_ranks = [
                t[0] for t in sorted(ranks, key=lambda x: x[1], reverse=True)
            ]
            return full_house, sorted_ranks

    """
    Three-of-a-kind (three cards of the same rank).
    Tiebreaker is first the rank of the three cards, then the highest other rank, then the second highest other rank.
    """
    for i in range(12, 4, -1):
        for key, value in counter.items():
            if value == 3:
                three_of_a_kind = "three-of-a-kind"
                ranks = []
                for ky, vl in rank_suit:
                    if key != CardRank[ky]:
                        ranks.append(ky)
                ranks = list(set(ranks))
                ranks.sort(reverse=True)
                caranks = []
                for ra in ranks:
                    caranks.append(CardRank[ra])
                return three_of_a_kind, [str(key)] + caranks[:2]

    """
    Two pair (two cards of the same rank, two cards of another rank).
    Tiebreaker is first the rank of the high pair, then the rank of the low pair and then the rank of the remaining card.
    """
    for i in range(12, 4, -1):
        ranks = []
        for key, value in counter.items():
            if value == 2:
                ranks.append(key)
            if len(ranks) == 2:
                ranks = sorted(ranks, key=lambda x: CardRank.index(x), reverse=True)
                two_pair = "two pair"
                ronks = []
                for ky, vl in rank_suit:
                    if ranks[0] != CardRank[ky] and ranks[1] != CardRank[ky]:
                        ronks.append(ky)
                ronks = list(set(ronks))
                ronks.sort(reverse=True)
                caranks = []
                for ra in ronks:
                    caranks.append(CardRank[ra])
                return two_pair, ranks + [caranks[0]]

    for i in range(12, 4, -1):
        for key, value in counter.items():
            if value == 2:
                pair = "pair"
                ronks = []
                for ky, vl in rank_suit:
                    if key != CardRank[ky]:
                        ronks.append(ky)
                ronks = list(set(ronks))
                ronks.sort(reverse=True)
                caranks = []
                for ra in ronks:
                    caranks.append(CardRank[ra])
                return pair, [key] + caranks[0:3]

    ronks = []
    for ky, vl in rank_suit:
        ronks.append(ky)
    ronks = list(set(ronks))
    ronks.sort(reverse=True)
    caranks = []
    for ra in ronks:
        caranks.append(CardRank[ra])
    return "nothing", caranks[0:5]


if __name__ == "__main__":
    print(
        1,
        hand(["K♥", "7♦"], ["5♦", "10♣", "6♦", "4♦", "3♦"])
        == ("straight-flush", ["7", "6", "5", "4", "3"]),
    )
    print(
        2,
        hand(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"])
        == ("straight-flush", ["J", "10", "9", "8", "7"]),
    )
    print(
        3,
        hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"])
        == ("flush", ["Q", "J", "10", "5", "3"]),
    )
    print(
        4,
        hand(["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"])
        == ("four-of-a-kind", ["2", "3"]),
    )
    print(
        5,
        hand(["A♠", "A♦"], ["K♣", "K♥", "A♥", "Q♥", "3♦"])
        == ("full house", ["A", "K"]),
    )
    print(
        6,
        hand(["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"])
        == ("straight", ["K", "Q", "J", "10", "9"]),
    )
    print(
        7,
        hand(["4♠", "9♦"], ["J♣", "Q♥", "Q♠", "2♥", "Q♦"])
        == ("three-of-a-kind", ["Q", "J", "9"]),
    )
    print(
        8,
        hand(["K♠", "J♦"], ["J♣", "K♥", "9♥", "2♥", "3♦"])
        == ("two pair", ["K", "J", "9"]),
    )
    print(
        9,
        hand(["K♠", "Q♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"])
        == ("pair", ["Q", "K", "J", "9"]),
    )
    print(
        10,
        hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"])
        == ("nothing", ["A", "K", "Q", "J", "9"]),
    )
    print(
        11,
        hand(["3♥", "7♣"], ["3♠", "9♠", "3♣", "8♦", "3♦"])
        == ("four-of-a-kind", ["3", "9"]),
    )
    print(
        12,
        hand(["2♣", "9♠"], ["9♣", "4♥", "7♣", "2♠", "K♠"])
        == ("two pair", ["9", "2", "K"]),
    )
    print(
        13,
        hand(["7♦", "3♥"], ["6♦", "7♥", "4♥", "3♦", "3♠"])
        == ("full house", ["3", "7"]),
    )
    print(
        14,
        hand(["J♠", "4♠"], ["9♠", "3♠", "5♠", "9♣", "2♠"])
        == ("flush", ["J", "9", "5", "4", "3"]),
    )
    print(
        13,
        hand(["4♦", "3♥"], ["J♥", "6♣", "5♠", "4♠", "2♣"])
        == ("straight", ["6", "5", "4", "3", "2"]),
    )
    print(
        14,
        hand(["A♥", "J♥"], ["K♠", "A♦", "J♦", "7♣", "3♥"])
        == ("two pair", ["A", "J", "K"]),
    )
    print(
        15,
        hand(["8♠", "10♣"], ["2♦", "9♥", "9♣", "10♠", "J♣"])
        == ("two pair", ["10", "9", "J"]),
    )
    print(
        1,
        hand(["9♠", "6♠"], ["10♠", "J♦", "7♠", "8♥", "8♠"])
        == ("straight-flush", ["10", "9", "8", "7", "6"]),
    )
    # print(1, hand() == )
