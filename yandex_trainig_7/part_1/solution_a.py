from operator import itemgetter


def distribute(groups: list[int], capacities: list[int]) -> list[int]:
    distribution = [0] * len(groups)
    rooms = sorted(enumerate(capacities), reverse=True, key=itemgetter(1))
    next_room = 0
    for group, count in sorted(enumerate(groups), reverse=True, key=itemgetter(1)):
        if next_room == len(rooms):
            break
        room, capacity = rooms[next_room]
        if count + 1 > capacity:
            continue
        distribution[group] = room + 1
        next_room += 1

    return distribution


def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    assert len(x) == n
    assert len(y) == m
    distribution = distribute(x, y)
    print(sum(map(bool, distribution)))
    print(*distribution, sep=" ")


if __name__ == "__main__":
    main()
