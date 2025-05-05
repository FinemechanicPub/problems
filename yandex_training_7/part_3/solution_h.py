import sys


class Fenwick:
    def __init__(self, n, cls, *parameters):
        self.fenwick = issubclass(cls, Fenwick)
        self.tree = [cls(*parameters) for _ in range(n)]

    def add(self, delta: int, *indices: int):
        index, *rest = indices
        while index < len(self.tree):
            if self.fenwick:
                self.tree[index].add(delta, *rest)
            else:
                self.tree[index] += delta
            index |= index + 1

    def sum_prefix(self, *indices: int) -> int:
        index, *rest = indices
        accumulator = 0
        index += 1
        while index > 0:
            index -= 1
            if self.fenwick:
                accumulator += self.tree[index].sum_prefix(*rest)
            else:
                accumulator += self.tree[index]
            index &= index + 1
        return accumulator


def cube(tree: Fenwick, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int):
    return (
        tree.sum_prefix(x2, y2, z2)
        - tree.sum_prefix(x1 - 1, y2, z2)
        - tree.sum_prefix(x2, y1 - 1, z2)
        - tree.sum_prefix(x2, y2, z1 - 1)
        + tree.sum_prefix(x2, y1 - 1, z1 - 1)
        + tree.sum_prefix(x1 - 1, y2, z1 - 1)
        + tree.sum_prefix(x1 - 1, y1 - 1, z2)
        - tree.sum_prefix(x1 - 1, y1 - 1, z1 - 1)
    )


def read(func=input):
    n = int(func())
    data = []
    while True:
        mode, *rest = func().split()
        if mode == "3":
            break
        data.append((mode, rest))
    return n, data


def process(n: int, data: list[tuple[str, list]]):
    tree = Fenwick(n, Fenwick, n, Fenwick, n, int)
    results: list[int] = []
    for mode, rest in data:
        if mode == "1":
            x, y, z, k = map(int, rest)
            tree.add(k, x, y, z)
        elif mode == "2":
            results.append(cube(tree, *map(int, rest)))
        else:
            assert False, f"Method \"{mode}\" not allowed"
    return results


if __name__ == "__main__":
    n, data = read(func=sys.stdin.readline)
    results = process(n, data)
    sys.stdout.write("\n".join(map(str, results)))
