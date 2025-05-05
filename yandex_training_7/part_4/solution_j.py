import sys
from typing import Self

BANKRUPTCY = 1
SPLIT = 2


class Enterprise:
    def __init__(self, length: int, next: Self | None, prev: Self | None):
        self.length = length
        self.next = next
        self.prev = prev


class CurrencyManager:
    def __init__(self, enterprise: Enterprise, position: int):
        self.enterprise = enterprise
        self.position = position

    def forward(self, target: int):
        while self.enterprise.next and self.position != target:
            self.enterprise = self.enterprise.next
            self.position += 1

    def backward(self, target: int):
        while self.enterprise.prev and self.position != target:
            self.enterprise = self.enterprise.prev
            self.position -= 1

    def move_to(self, target: int):
        if target > self.position:
            self.forward(target)
        elif target < self.position:
            self.backward(target)

    def delete(self):
        self.enterprise.prev.next = self.enterprise.next
        self.enterprise.next.prev = self.enterprise.prev
        self.enterprise = self.enterprise.next

    def insert_after(self, enterprise: Enterprise):
        if self.enterprise.next:
            self.enterprise.next.prev = enterprise
        enterprise.next = self.enterprise.next
        self.enterprise.next = enterprise
        enterprise.prev = self.enterprise


def process(lengths: list[int], events: list[tuple[int, int]]) -> list[int]:
    squares = [sum(length * length for length in lengths)]

    head = enterprise = Enterprise(-1, None, None)
    for length in lengths:
        enterprise.next = Enterprise(length, None, enterprise)
        enterprise = enterprise.next
    enterprise.next = tail = Enterprise(-1, None, enterprise)

    assert head.next
    current = CurrencyManager(head.next, 1)

    for event, entity in events:
        current.move_to(entity)
        assert current.enterprise.next
        assert current.enterprise.prev
        length = current.enterprise.length
        to_left = length // 2
        to_right = length - to_left
        squares.append(squares[-1] - current.enterprise.length ** 2)
        if event == BANKRUPTCY:
            if current.enterprise.prev is head:
                squares[-1] -= current.enterprise.next.length ** 2
                current.enterprise.next.length += length
                squares[-1] += current.enterprise.next.length ** 2
            elif current.enterprise.next is tail:
                squares[-1] -= current.enterprise.prev.length ** 2
                current.enterprise.prev.length += length
                squares[-1] += current.enterprise.prev.length ** 2
            else:
                squares[-1] -= current.enterprise.prev.length ** 2
                squares[-1] -= current.enterprise.next.length ** 2
                current.enterprise.prev.length += to_left
                current.enterprise.next.length += to_right
                squares[-1] += current.enterprise.prev.length ** 2
                squares[-1] += current.enterprise.next.length ** 2
        elif event == SPLIT:
            current.insert_after(Enterprise(to_right, None, None))
            squares[-1] += current.enterprise.next.length ** 2
            current.insert_after(Enterprise(to_left, None, None))
            squares[-1] += current.enterprise.next.length ** 2
        current.delete()
    return squares


if __name__ == "__main__":
    reader = sys.stdin.readline
    n = int(reader())
    a = list(map(int, reader().split()))
    k = int(reader())
    events: list[tuple[int, int]] = []
    for _ in range(k):
        e, v = map(int, reader().split())
        events.append((e, v))
    squares = process(a, events)
    sys.stdout.write("\n".join(map(str, squares)))
