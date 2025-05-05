# Полиномиальные хэши

import sys
from typing import Callable, TypeAlias


NodeType: TypeAlias = tuple[int, int]


class HashProvider:
    def __init__(self, length: int, mod: int, base: int):
        self.mod = mod
        self.powers = [1]
        self.sum_powers = [1]
        for i in range(1, length):
            self.powers.append(self.powers[i - 1] * base % mod)
            self.sum_powers.append(
                (self.sum_powers[i - 1] + self.powers[i]) % mod
            )

    def sequence(self, value: int, length: int):
        return value * self.sum_powers[length - 1] % self.mod


def concatenate(a: NodeType, b: NodeType, provider: HashProvider):
    if a[1] == 0:
        return b
    if b[1] == 0:
        return a
    return (
        (b[0] + a[0] * provider.powers[b[1]]) % provider.mod,  # hash
        a[1] + b[1]  # length
    )


class SegmentTreeBase:
    def __init__(
            self,
            items: list[NodeType],
            merger: Callable[[NodeType, NodeType, HashProvider], NodeType],
            provider: HashProvider,
            neutral: NodeType
    ):
        self.merger = merger
        self.provider = provider
        self.neutral = neutral
        self.max_index = self.power_two_length(len(items)) - 1
        self.storage_base = self.max_index
        self.storage_length = 2 * self.max_index + 1
        self.defer = [0] * self.storage_length
        self.items = (
            [neutral] * self.storage_base
            + items
            + [neutral] * (self.max_index - len(items) + 1)
        )
        for i in reversed(range(self.storage_base)):
            self.items[i] = self.merge_children(i)

    def merge_children(self, i: int):
        return self.merger(
            self.items[2 * i + 1], self.items[2 * i + 2], self.provider
        )

    def _propagate_defer(self, i: int):
        defer = self.defer[i]
        child_length = self.items[i][1] // 2
        hash = self.provider.sequence(defer, child_length)
        self.items[2 * i + 1] = (hash, child_length)
        self.items[2 * i + 2] = (hash, child_length)
        if child_length > 1:
            self.defer[2 * i + 1] = defer
            self.defer[2 * i + 2] = defer
        self.defer[i] = 0

    def update_defer(self, left: int, right: int, value: int):
        def _update_defer(i: int, my_left: int, my_right: int):
            my_length = self.items[i][1]
            if left <= my_left and right >= my_right:
                hash = self.provider.sequence(value, my_length)
                self.items[i] = (hash, my_length)
                if my_length > 1:
                    self.defer[i] = value
                return self.items[i]
            if left > my_right or right < my_left:
                return self.items[i]  # no update: return stored value
            if self.defer[i]:
                self._propagate_defer(i)
            mid = (my_left + my_right) // 2
            self.items[i] = self.merger(
                _update_defer(2 * i + 1, my_left, mid),
                _update_defer(2 * i + 2, mid + 1, my_right),
                self.provider
            )
            return self.items[i]

        return _update_defer(0, 0, self.max_index)

    def get(self, left: int, right: int):
        def _get(i, my_left: int, my_right: int):
            if left <= my_left and right >= my_right:
                return self.items[i]
            if left > my_right or right < my_left:
                return self.neutral
            mid = (my_left + my_right) // 2
            if self.defer[i]:
                self._propagate_defer(i)
            return self.merger(
                _get(2 * i + 1, my_left, mid),
                _get(2 * i + 2, mid + 1, my_right),
                self.provider
            )

        return _get(0, 0, self.max_index)

    @staticmethod
    def power_two_length(length: int):
        """
        >>> SegmentTreeBase.power_two_length(1)
        1
        >>> SegmentTreeBase.power_two_length(2)
        2
        >>> SegmentTreeBase.power_two_length(3)
        4
        """
        n = 1
        while n < length:
            n <<= 1
        return n


class HashTree(SegmentTreeBase):
    NEUTRAL = (0, 0)

    def __init__(self, nums: list[int], provider: HashProvider):
        super().__init__(
            [(num, 1) for num in nums], concatenate, provider, self.NEUTRAL
        )

    def update_defer(self, left: int, right: int, value: int):
        if value:
            return super().update_defer(left - 1, right - 1, value)
        return None

    def compare(self, first: int, second: int, length: int):
        if first == second:
            return True
        return (
            self.get(first - 1, first + length - 2)
            == self.get(second - 1, second + length - 2)
        )


def read(reader=input):
    n = int(reader())
    nums = list(map(int, reader().split()))
    assert len(nums) == n
    m = int(reader())
    queries = [reader().split() for _ in range(m)]
    return nums, queries


def process(tree: HashTree, queries: list[tuple[str, ...]]):
    result: list[str] = []
    for request, *operands in queries:
        if request == "0":
            tree.update_defer(*map(int, operands))
        elif request == "1":
            result.append("+" if tree.compare(*map(int, operands)) else "-")
        else:
            assert False, f"Unknown request \"{request}\""
    return result


def write(results: list[str]):
    sys.stdout.write("".join(results))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "rt") as file:
            nums, queries = read(file.readline)
    else:
        nums, queries = read()
    tree = HashTree(nums, HashProvider(len(nums), 1000003999, 102013))
    result = process(tree, queries)
    write(result)
