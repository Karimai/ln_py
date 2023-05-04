"""
https://www.codewars.com/kata/524c74f855025e2495000262/train/python
"""


import random
import re


def split(card):
    rank_suit = []
def split(card: str):
    # Define the regular expression pattern
    pattern = r'^\d{1,2}|[JQK]'
    re_match = re.search(pattern, card)
    rank = re_match.group(0)
    rank_suit = []
    card.replace(card, rank)

    match rank:
        case 'J':
            return 10
        case 'Q':
            return 11
        case 'K':
            return 12
        case _:
            return int(rank) - 1


def five_concecutive(hole_cards, community_cards):
    straight = ""
    flush = ""
    validation = [True] * 5
    init_lst = [False] * 13
    pattern = r'^\d{1,2}|[AJQK]'
    rank_suit = []
    for card in hole_cards + community_cards:
        re_match = re.search(pattern, card)
        rank = re_match.group(0)
        suit = card.replace(rank, '')
        match rank:
            case 'A':
                rank_suit.append((0, suit),)
                init_lst[0] = True
            case 'J':
                rank_suit.append((10, suit),)
                init_lst[10] = True
            case 'Q':
                rank_suit.append((11, suit),)
                init_lst[1] = True
            case 'K':
                rank_suit.append((12, suit),)
                init_lst[12] = True
            case _:
                rank_suit.append((int(rank) - 1, suit),)
                init_lst[int(rank) - 1] = True

    for i in range(13-5):
        if all(init_lst[i+j] * validation[j] for j in range(5)):
            straight = "straight"
        for s in '♠♦♥♣':
            if sum(1 for x in rank_suit if x[1] == s) >= 5:
                flush = "flush"
            if sum(1 for x in rank_suit if x[1] == s) >= 4:
                four_of_a_kind = "four of a kind"
                return four_of_a_kind

    return " ".join([straight, flush]).strip()


if __name__ == "__main__":
    print(five_concecutive(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]) == ("straight-flush", ["J", "10", "9", "8", "7"]))
    print(five_concecutive(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]) == "flush")
    print(five_concecutive(["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"] == "four-of-a-kind"))
