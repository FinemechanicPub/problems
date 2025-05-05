def connect(n: int, bridges: list[tuple[int, int]]) -> int:
    parent = list(range(n))
    size = [1] * n

    def find(island: int):
        if parent[island] != island:
            parent[island] = find(parent[island])
        return parent[island]

    def union(island_a: int, island_b: int):
        parent_a = find(island_a)
        parent_b = find(island_b)
        if parent_a == parent_b:
            return
        if size[parent_a] > size[parent_b]:
            parent_a, parent_b = parent_b, parent_a
        parent[parent_a] = parent_b
        size[parent_b] += size[parent_a]
        return size[parent_b]

    for step, (island_a, island_b) in enumerate(bridges, start=1):
        if union(island_a - 1, island_b - 1) == n:
            return step
    return n


if __name__ == "__main__":
    n, m = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(m)]
    assert len(bridges) == m, f"Expected {m} bridges, got {len(bridges)}"
    assert all(len(bridge) == 2 for bridge in bridges)
    print(connect(n, bridges))  # type: ignore
