def count_broken(pigs: list[int]) -> int:
    parent = list(range(len(pigs)))
    size = [1] * len(pigs)

    def find(pig: int):
        if parent[pig] != pig:
            parent[pig] = find(parent[pig])
        return parent[pig]

    def union(pig_a: int, pig_b: int):
        parent_a = find(pig_a)
        parent_b = find(pig_b)
        if parent_a == parent_b:
            return
        if size[parent_a] > size[parent_b]:
            parent_a, parent_b = parent_b, parent_a
        parent[parent_a] = parent_b
        size[parent_b] += size[parent_a]

    for pig, key in enumerate(pigs):
        union(pig, key - 1)

    return sum(parent[i] == i for i in range(len(parent)))


if __name__ == "__main__":
    n = int(input())
    pigs = [int(input()) for _ in range(n)]
    print(count_broken(pigs))
