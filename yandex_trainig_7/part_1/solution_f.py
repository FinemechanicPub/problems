def backpack(max_weight: int, masses: list[int], costs: list[int]):
    """
    >>> backpack(6, [2, 4, 1, 2], [7, 2, 5, 1])
    [1, 3, 4]
    >>> backpack(1, [2, 4, 5, 2], [7, 2, 5, 1])
    []
    >>> backpack(9, [3, 2, 3, 2, 2, 3], [1, 5, 1, 5, 2, 1])
    [1, 2, 4, 5]
    >>> backpack(4, [2, 4, 5, 2], [7, 2, 5, 1])
    [1, 4]
    >>> backpack(15, [5, 5, 8, 10], [2, 5, 2, 2])
    [1, 2]
    """
    pack = [(-1, -1)] * (max_weight + 1)
    pack[0] = (0, 0)
    packs = [pack]
    for mass, cost in zip(masses, costs):
        pack = packs[-1].copy()
        for weight in reversed(range(max_weight - mass + 1)):
            old_cost, _ = pack[weight]
            if old_cost >= 0 and old_cost + cost > pack[weight + mass][0]:
                pack[weight + mass] = (old_cost + cost, len(packs))
        packs.append(pack)

    pieces = []
    weight, _ = max(enumerate(packs[-1]), key=lambda x: x[1][0])
    pack_index = len(packs) - 1
    while pack_index > 0 and weight > 0:
        pack = packs[pack_index]
        while weight and pack[weight][1] == -1:
            weight -= 1
        if not weight:
            break
        _, piece = pack[weight]
        pieces.append(piece)
        weight -= masses[piece - 1]
        pack_index = piece - 1
    return pieces[::-1]


def main():
    n, m = map(int, input().split())
    masses = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    assert len(masses) == n
    assert len(costs) == n
    print(*backpack(m, masses, costs), sep="\n")


if __name__ == "__main__":
    main()
