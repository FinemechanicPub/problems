from collections import defaultdict
from operator import itemgetter


def group_by_item(
        bricks: list[tuple[int, int, int]], item: int
) -> dict[int, list[tuple[int, int, int]]]:
    """
    >>> dict(group_by_item([(1, 1, 1), (2, 2, 1), (3, 3, 1)], 2))
    {1: [(1, 1, 1), (2, 2, 1), (3, 3, 1)]}
    >>> dict(group_by_item([(1, 1, 1), (2, 1, 2), (3, 2, 1), (4, 2, 2)], 2))
    {1: [(1, 1, 1), (3, 2, 1)], 2: [(2, 1, 2), (4, 2, 2)]}
    """
    groups: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for brick in bricks:
        groups[brick[item]].append(brick)
    return groups


def backpack(bricks: list[int], max_length: int = 0) -> dict[int, int]:
    """
    >>> backpack([1, 2, 3])
    {1: 0, 2: 1, 3: 1, 4: 2, 5: 2}
    >>> backpack([1, 2])
    {1: 0, 2: 1}
    >>> backpack([3])
    {}
    """
    max_length = max_length or (sum(bricks) - min(bricks))
    lengths = [-1] * (max_length + 1)
    lengths[0] = 0
    last_length = 0
    for i, brick in enumerate(bricks):
        top = min(last_length, max_length - brick) + 1
        for length in reversed(range(top)):
            if lengths[length] >= 0 and lengths[length + brick] == -1:
                lengths[length + brick] = i
                last_length = max(last_length, length + brick)
    return {
        length: i for length, i in enumerate(lengths) if i >= 0 and length > 0
    }


def restore(
        length: int, pack: dict[int, int], bricks: list[tuple[int, int, int]]
) -> list[int]:
    row = []
    while length > 0:
        brick_id, brick_length, _ = bricks[pack[length]]
        row.append(brick_id)
        length -= brick_length
    return row


def build(bricks: list[tuple[int, int, int]], max_color: int) -> list[int]:
    """
    >>> build([(1, 1, 1), (2, 2, 1), (3, 3, 1)], 1)
    [1]
    >>> build([(1, 1, 1), (2, 2, 1), (3, 3, 2)], 2)
    []
    >>> build([(1, 1, 1)], 1)
    []
    """
    wall: list[int] = []
    bricks.sort(key=itemgetter(1))
    colors = group_by_item(bricks, 2)
    common_lengths: set[int] = set()
    backpacks = []
    for group in colors.values():
        backpacks.append(backpack(
            [length for _, length, _ in group],
            max(common_lengths, default=0))
        )
        if not common_lengths:
            common_lengths.update(backpacks[-1])
        else:
            common_lengths &= backpacks[-1].keys()
        if not common_lengths:
            break
    length = next(iter(common_lengths), 0)
    if length:
        for pack, group in zip(backpacks, colors.values()):
            wall.extend(restore(length, pack, group))
    return sorted(wall)


def read() -> tuple[int, list[tuple[int, int, int]]]:
    n, k = map(int, input().split())
    bricks = []
    for i in range(n):
        l, c = map(int, input().split())
        bricks.append((i+1, l, c))
    return k, bricks


def main():
    k, bricks = read()
    wall = build(bricks, k)
    print("YES" if wall else "NO")
    print(*wall, sep=" ")


if __name__ == "__main__":
    main()
