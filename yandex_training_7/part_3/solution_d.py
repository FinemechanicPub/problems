def ror(n: int, length: int) -> int:
    carry = n & 1
    n >>= 1
    if carry:
        n |= 1 << (length - 1)
    return n


def solve(n: int) -> int:
    max_n = n
    length = n.bit_length()
    for _ in range(length):
        n = ror(n, length)
        max_n = max(max_n, n)
    return max_n


if __name__ == "__main__":
    n = int(input())
    print(solve(n))
