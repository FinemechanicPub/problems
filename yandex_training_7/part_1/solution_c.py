from fractions import Fraction
from functools import cache

GRADES = 31


def minimal_cost(duration: int, card_seconds: list[int]) -> int:
    """
    >>> minimal_cost(11, [1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    5
    >>> minimal_cost(4, [3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    2
    """
    cards = sorted(
        ((seconds, 1 << i) for i, seconds in enumerate(card_seconds)),
        key=lambda x: Fraction(x[1], x[0])
    )

    @cache
    def calculate(time_left, card_index):
        seconds, price = cards[card_index]
        number, remainder = divmod(time_left, seconds)
        min_amount = number * price
        if not remainder:
            return min_amount
        if card_index + 1 == len(cards):
            return min_amount + price
        return min_amount + min(price, calculate(remainder, card_index + 1))

    return calculate(duration, 0)


if __name__ == "__main__":
    m = int(input())
    a = list(map(int, input().split()))
    assert len(a) == GRADES, f"Got {len(a)} cards, should have gotten {GRADES} instead"
    print(minimal_cost(m, a))
