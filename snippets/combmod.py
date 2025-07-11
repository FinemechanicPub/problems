def comb_mod_frac(n: int, k: int, mod: int) -> tuple[int, int]:
    numerator, denominator = 1, 1
    k = min(k, n - k)
    m = n - k
    for factor in range(1, k + 1):
        denominator = denominator * factor % mod
        numerator = numerator * ((m + factor) % mod) % mod
    return numerator, denominator


def comb_mod(n: int, k: int, mod: int, inv: bool = False) -> int:
    """
    Вычисление числа сочетаний по модулю
    >>> import math; comb_mod(5, 3, 7) == math.comb(5, 3) % 7
    True
    >>> import math; comb_mod(5, 3, 7, True) * math.comb(5, 3) % 7
    1
    """
    numerator, denominator = comb_mod_frac(n, k, mod)
    if inv:
        numerator, denominator = denominator, numerator
    return pow(denominator, mod - 2, mod) * numerator % mod
