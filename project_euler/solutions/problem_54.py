from collections import Counter
from enum import IntEnum, Enum
from functools import total_ordering

from typing import Iterable, NamedTuple, List, Tuple

from ..framework.load_file import load_file


class Value(IntEnum):
    low_ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    ace = 14

    @classmethod
    def from_str(cls, name: str) -> "Value":
        try:
            if name == 'T':
                number = 10
            else:
                number = int(name)

            for value_name, value in cls.__members__.items():
                if value.value == number:
                    return value
        except ValueError:
            for value_name, value in cls.__members__.items():
                if value_name[0] == name[0].lower():
                    return value

        raise ValueError(f'Failed to create value from name {name}.')


class Suit(Enum):
    clubs = 0
    diamonds = 1
    hearts = 2
    spades = 3

    @classmethod
    def from_str(cls, name: str) -> "Suit":
        for value_name, value in cls.__members__.items():
            if value_name[0] == name[0].lower():
                return value

        raise ValueError(f'Failed to create suit from name {name}.')


class Kind(IntEnum):
    high_card = 0
    one_pair = 1
    two_pair = 2
    three_of_a_kind = 3
    straight = 4
    flush = 5
    full_house = 6
    four_of_a_kind = 7
    straight_flush = 8  # don't need royal flush: highest straight flush


Card = NamedTuple('Card', [('value', Value), ('suit', Suit)])
Hand = Tuple[Card, Card, Card, Card]


def hands_from_line(line: str) -> Tuple[Hand, Hand]:
    cards = tuple(Card(Value.from_str(v), Suit.from_str(s))
                  for v, s in line.split(' '))

    return cards[:5], cards[5:]


@total_ordering
class PokerResult:
    def __init__(self, kind: Kind, data: List[int]) -> None:
        self.kind = kind
        self.data = data

    def __eq__(self, other) -> bool:
        return self.kind == other.kind and self.data == other.data

    def __lt__(self, other) -> bool:
        if self.kind != other.kind:
            return self.kind < other.kind
        for self_datum, other_datum in zip(self.data, other.data):
            if self_datum != other_datum:
                return self_datum < other_datum

    @classmethod
    def from_hand(cls, hand: Hand) -> "PokerResult":
        # suit based
        flush = (len(set(suit for _, suit in hand)) == 1)

        def lrs(iterable: Iterable) -> List:
            return list(reversed(sorted(iterable)))

        # value based
        values = set(value for value, _ in hand)
        counter = Counter(value for value, _ in hand)
        straight = sorted(counter) in [list(range(n, n + 5)) for n
                                       in range(2, 10)] + [[2, 3, 4, 5, 14]]

        if len(counter) == 2:
            four_of_a_kind = max(counter.values()) == 4
            full_house = max(counter.values()) == 3

            assert four_of_a_kind or full_house

            four_full_hc = list(counter.most_common())
        else:
            four_of_a_kind = False
            full_house = False

        if straight and flush:
            return PokerResult(Kind.straight_flush, [min(counter)])
        if four_of_a_kind:
            return PokerResult(Kind.four_of_a_kind, four_full_hc)
        if full_house:
            return PokerResult(Kind.full_house, four_full_hc)
        if flush:
            return PokerResult(Kind.flush, lrs(values))
        if straight:
            if Value.ace in counter:
                PokerResult(Kind.straight, [Value.low_ace])
            return PokerResult(Kind.straight, min([value for value in hand]))

        if len(counter) == 3:
            if max(counter.values()) == 3:
                three = counter.most_common(1)[0]
                high_cards = lrs(counter.most_common()[1:])
                return PokerResult(Kind.three_of_a_kind, [three] + high_cards)
            else:
                pairs = lrs(counter.most_common(2))
                high_card = counter.most_common()[2:]
                return PokerResult(Kind.two_pair, pairs + high_card)

        if len(counter) == 4:
            pair = counter.most_common(1)
            high_cards = lrs(counter.most_common()[1:])

            return PokerResult(Kind.one_pair, pair + high_cards)

        high_cards = lrs(counter)
        return PokerResult(Kind.high_card, high_cards)


def solve(name: str='poker.txt', relative: bool=True) -> int:
    hands_raw = load_file(54, name, relative)

    lines = hands_raw.split('\n')

    wins_player_1 = 0

    for line in lines:
        if line == '':
            continue
        hand1, hand2 = hands_from_line(line)

        result1 = PokerResult.from_hand(hand1)
        result2 = PokerResult.from_hand(hand2)

        if result1 > result2:
            wins_player_1 += 1

    return wins_player_1
