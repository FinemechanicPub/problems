from functools import reduce
from operator import or_


def block_ham(block: str):
    """
    >>> block_ham("0100010000111101")
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1]
    """
    result: list[int] = []
    index = 1
    for bit in block:
        while index.bit_count() == 1:
            result.append(1)
            index += 1
        value = 1 if bit == "1" else 0
        result.append(value)
        mask = 1
        while mask < index:
            if index & mask:
                result[mask - 1] ^= value
            mask <<= 1
        index += 1
    return result


def block_unham(block: str):
    """
    >>> block_unham("010010010100001111101")
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
    >>> block_unham("110010010100001111101")
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
    >>> block_unham("000010010100001111101")
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
    >>> block_unham("010010010100001111100")
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
    >>> block_unham("010010010100101111101")
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
    >>> block_unham("000111111011000100001001001111")
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1]

    """
    result: list[int] = []
    parity: dict[int, int] = dict()
    for index, bit in enumerate(block, start=1):
        value = 1 if bit == "1" else 0
        if index.bit_count() == 1:
            parity[index] = value
            continue
        result.append(value)
        mask = 1
        while mask in parity:
            if mask & index:
                parity[mask] ^= value
            mask <<= 1
    bad_index = reduce(or_, (index for index, p in parity.items() if not p), 0)
    if bad_index.bit_count() > 1:
        bit_length = bad_index.bit_length()
        result[bad_index - bit_length - 1] ^= 1
    return result


def ham(x: str) -> str:
    return "".join(map(str, block_ham(x)))


def unham(z: str) -> str:
    return "".join(map(str, block_unham(z)))


if __name__ == "__main__":
    mode = int(input())
    if mode == 1:
        x = input()
        y = ham(x)
        print(y, flush=True)
    elif mode == 2:
        z = input()
        x = unham(z)
        print(x, flush=True)
