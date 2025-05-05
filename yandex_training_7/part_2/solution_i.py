import sys
from typing import Callable, TypeAlias


NodeType: TypeAlias = int


def max_node(a: NodeType, b: NodeType) -> NodeType:
    return max(a, b)


class SegmentTreeBase:
    def __init__(
            self,
            items: list[NodeType],
            merger: Callable[[NodeType, NodeType], NodeType],
            neutral: NodeType
    ):
        self.merger = merger
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
        return self.merger(self.items[2 * i + 1], self.items[2 * i + 2])

    def update(self, index: int, value: NodeType):
        i = self.storage_base + index
        self.items[i] = value
        while i:
            i = (i - 1) >> 1
            update_value = self.merge_children(i)
            if self.items[i] == update_value:
                break
            self.items[i] = update_value
        return self

    def update_defer_add(self, left: int, right: int, delta: int):
        def _update_defer(i: int, my_left: int, my_right: int):
            if left <= my_left and right >= my_right:
                self.items[i] += delta
                self.defer[i] += delta
                return self.items[i]
            if left > my_right or right < my_left:
                return self.items[i]  # self.neutral
            if self.defer[i]:
                defer = self.defer[i]
                child_1 = 2 * i + 1
                child_2 = 2 * i + 2
                self.items[child_1] += defer
                self.defer[child_1] += defer
                self.items[child_2] += defer
                self.defer[child_2] += defer
                self.defer[i] = 0
            mid = (my_left + my_right) // 2
            self.items[i] = self.merger(
                _update_defer(2 * i + 1, my_left, mid),
                _update_defer(2 * i + 2, mid + 1, my_right),
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
                defer = self.defer[i]
                child_1 = 2 * i + 1
                child_2 = 2 * i + 2
                self.items[child_1] += defer
                self.defer[child_1] += defer
                self.items[child_2] += defer
                self.defer[child_2] += defer
                self.defer[i] = 0

            return self.merger(
                _get(2 * i + 1, my_left, mid),
                _get(2 * i + 2, mid + 1, my_right)
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


class MaxTree(SegmentTreeBase):
    NEUTRAL = -1

    def __init__(self, nums: list[int]):
        super().__init__(nums, max_node, self.NEUTRAL)

    def update_defer_add(self, left: int, right: int, value: int):
        if value:
            return super().update_defer_add(left - 1, right - 1, value)
        return None

    def get(self, left: int, right: int):
        return super().get(left - 1, right - 1)


def read(reader=input):
    n = int(reader())
    nums = list(map(int, reader().split()))
    assert len(nums) == n
    m = int(reader())
    queries = [reader().split() for _ in range(m)]
    return nums, queries


def process(tree: MaxTree, queries: list[tuple[str, ...]]):
    result: list[str] = []
    for request, *operands in queries:
        if request == "a":
            tree.update_defer_add(*map(int, operands))
        elif request == "m":
            result.append(str(tree.get(*map(int, operands))))
        else:
            assert False, f"Unknown request \"{request}\""
    return result


def write(results: list[str]):
    sys.stdout.write(" ".join(results))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "rt") as file:
            nums, queries = read(file.readline)
    else:
        nums, queries = read()
    tree = MaxTree(nums)
    result = process(tree, queries)
    write(result)
