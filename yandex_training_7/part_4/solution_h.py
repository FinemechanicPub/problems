import sys


def process(n: int, operations: list[tuple[str, int, int]]) -> list[str]:
    parent = list(range(n))
    size = [1] * n

    def find(node: int):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node_a: int, node_b: int):
        parent_a = find(node_a)
        parent_b = find(node_b)
        if parent_a == parent_b:
            return
        if size[parent_a] > size[parent_b]:
            parent_a, parent_b = parent_b, parent_a
        parent[parent_a] = parent_b
        size[parent_b] += size[parent_a]
        return size[parent_b]

    answers = []
    for operation, node_a, node_b in reversed(operations):
        if operation == "cut":
            union(node_a - 1, node_b - 1)
        elif operation == "ask":
            answers.append(
                "YES" if find(node_a - 1) == find(node_b - 1) else "NO"
            )
    return answers[::-1]


if __name__ == "__main__":
    reader = sys.stdin.readline
    n, m, k = map(int, reader().split())
    for _ in range(m):
        reader()
    operations = []
    for _ in range(k):
        operation, *nodes = reader().split()
        node_a, node_b = map(int, nodes)
        operations.append((operation, node_a, node_b))
    sys.stdout.write("\n".join(process(n, operations)))
