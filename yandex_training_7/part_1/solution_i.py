from operator import itemgetter


def pack_rover(base_volume, items):
    """
    >>> pack_rover(7, [(4, 1, 2), (3, 1, 2), (2, 1, 2)])
    [1, 2, 3]
    >>> pack_rover(7, [(4, 1, 3), (3, 1, 2), (2, 1, 1)])
    [2, 3]
    >>> pack_rover(2, [(1, 510578, 6), (400, 480916, 3), (1, 513164, 1), (317, 210463, 8), (460, 216209, 0), (515, 741869, 8)])
    [1, 3]
    """
    n = len(items)
    total_volume = sum(volume for volume, _, _ in items)
    if total_volume <= base_volume:
        return list(range(1, n + 1))
    MAX_VOLUME = total_volume

    indexed_items = sorted(
        ((i, *item) for i, item in enumerate(items, start=1)),
        key=itemgetter(3),
        reverse=True
    )

    pack = [(-1, -1, -1)] * (MAX_VOLUME + 1)
    pack[0] = (0, 0, 0)  # cost, id, ordinal
    packs = [pack]
    ROVER_PRESSURE = [
        max(0, volume - base_volume) for volume in range(len(pack))
    ]

    for id, volume, cost, pressure in indexed_items:
        pack = packs[-1].copy()
        for i in reversed(range(MAX_VOLUME - volume + 1)):
            if pressure < ROVER_PRESSURE[i + volume]:
                continue
            if pack[i][0] >= 0 and pack[i][0] + cost > pack[i + volume][0]:
                pack[i + volume] = (pack[i][0] + cost, id, len(packs))
        packs.append(pack)

    goods = []
    volume, _ = max(enumerate(packs[-1]), key=lambda x: x[1][0])
    i = len(packs) - 1
    while i > 0 and volume > 0:
        _, id, ordinal = packs[i][volume]
        volume -= items[id - 1][0]
        goods.append(id)
        i = ordinal - 1
    return sorted(goods)


def main():
    n, s = map(int, input().split())
    items = []
    for i in range(n):
        items.append(tuple(map(int, input().split())))
    goods = pack_rover(s, items)
    total_cost = sum(items[good - 1][1] for good in goods)
    print(len(goods), total_cost)
    print(*goods, sep=" ")


if __name__ == "__main__":
    main()
