
def primes(n: int) -> list[int]:
    """
    Возвращает список простых чисел в интервале [2, n)
    >>> primes(2)
    []
    >>> primes(3)
    [2]
    >>> primes(70)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
    """
    if n < 3:
        return []
    primes = [2]
    sieve = [True] * n
    for p in range(3, n, 2):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n, p):
                sieve[i] = False
    return primes
