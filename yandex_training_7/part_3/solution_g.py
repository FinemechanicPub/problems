class Fenwick:
    def __init__(self, n):
        self.tree = [0] * n
        self.items = [0] * n

    def replace(self, index: int, value: int):
        delta = value - self.items[index]
        self.items[index] = value
        while index < len(self.tree):
            self.tree[index] += delta
            index |= index + 1

    def sum(self, left: int, right: int) -> int:
        if left:
            return self._sum_prefix(right) - self._sum_prefix(left - 1)
        else:
            return self._sum_prefix(right)

    def _sum_prefix(self, index: int) -> int:
        accumulator = 0
        index += 1
        while index:
            index -= 1
            accumulator += self.tree[index]
            index &= index + 1
        return accumulator


if __name__ == "__main__":
    n, k = map(int, input().split())
    tree = Fenwick(n)
    for _ in range(k):
        request, *rest = input().split()
        if request == "A":
            index, value = map(int, rest)
            tree.replace(index - 1, value)
        elif request == "Q":
            left, right = map(int, rest)
            print(tree.sum(left - 1, right - 1))
        else:
            assert False, "Method not allowed"
