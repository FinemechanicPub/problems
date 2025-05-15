"""Функции умножения и возведения в степень для матриц"""


def matrix_mul(matrix_1: list[list[int]], matrix_2: list[list[int]], mod: int):
    n, m = len(matrix_1), len(matrix_2[0])
    result = [[0] * m for _ in range(n)]
    for row_1, result_row in zip(matrix_1, result):
        for factor, row_2 in zip(row_1, matrix_2):
            if not factor:
                continue
            for j in range(m):
                result_row[j] += factor * row_2[j]
        if mod:
            for i in range(len(result_row)):
                result_row[i] %= mod
    return result


def matrix_square(matrix: list[list[int]], mod: int):
    return matrix_mul(matrix, matrix, mod)


def matrix_exp(matrix: list[list[int]], n: int, mod: int = 0):
    """
    >>> matrix_exp([[1, 2], [3, 4]], 4)
    [[199, 290], [435, 634]]
    >>> matrix_exp([[1, 2], [3, 4]], 5)
    [[1069, 1558], [2337, 3406]]
    >>> matrix_exp([[1, 2], [3, 4]], 4, 11)
    [[1, 4], [6, 7]]
    >>> matrix_exp([[1, 2], [3, 4]], 5, 11)
    [[2, 7], [5, 7]]
    """
    if n == 1:
        return matrix
    if n == 2:
        return matrix_square(matrix, mod)
    temp = matrix_exp(matrix, n // 2, mod)
    if n & 1:
        return matrix_mul(
            temp, matrix_mul(matrix, temp, mod), mod
        )
    return matrix_square(temp, mod)
