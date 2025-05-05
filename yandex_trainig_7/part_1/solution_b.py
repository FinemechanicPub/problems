def sect(numbers: list[int]) -> list[int]:
    """
    >>> sect([1, 3, 3, 3, 2])
    [1, 3, 1]
    >>> sect([1, 9, 8, 7, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9])
    [1, 6, 9]
    >>> sect([7, 2, 3, 4, 3, 2, 7])
    [2, 3, 2]
    >>> sect([125])
    [1]
    >>> sect([5, 1, 1, 1, 1, 1])
    [1, 1, 1, 1, 1, 1]
    """
    sections: list[int] = [0]
    max_length = len(numbers)
    for number in numbers:
        if sections[-1] + 1 > number or sections[-1] == max_length:
            sections.append(1)
            max_length = number
        else:
            sections[-1] += 1
            max_length = min(max_length, number)
    return sections


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        assert len(a) == n
        sections = sect(a)
        print(len(sections))
        print(*sections, sep=" ")


if __name__ == "__main__":
    main()
