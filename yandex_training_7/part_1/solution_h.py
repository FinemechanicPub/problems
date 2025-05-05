def score(job: str) -> tuple[int, int]:
    """
    Score gained if job starts at odd or even day
    >>> score("DSD")
    (0, 1)
    >>> score("SS")
    (1, 1)
    >>> score("DD")
    (0, 0)
    >>> score("SDD")
    (1, 0)
    """
    return (
        job[0::2].count("S"),
        job[1::2].count("S"),
    )


def simple(jobs: list[str]) -> int:
    """
    >>> simple(["DSD", "SS", "DD", "SDD"])
    3
    >>> simple(["DSD", "SS", "DDS", "SDD"])
    4
    >>> simple(["S"])
    1
    >>> simple(["D"])
    0
    >>> simple(['SS', 'DDS', 'S', 'DD'])
    2
    >>> simple(['SD', 'SDDSS', 'SSSSDSDS', 'DSDDDSSD', 'SDSSDDS'])
    11
    >>> simple(['SDSDDSSDDS', 'SSDDSD', 'SDSSDSSDS', 'SSSDDSSDSS', 'DDDDSDD'])
    13
    """
    odd_jobs = sorted(
        (score(job) for job in jobs if len(job) & 1),
        key=lambda s: s[0] - s[1],
    )
    half = len(odd_jobs) // 2
    count = (
        sum(odd_jobs[i][1] for i in range(half))
        + sum(odd_jobs[i][0] for i in range(half, len(odd_jobs)))
    )
    if odd_jobs:
        count += sum(max(score(job)) for job in jobs if not len(job) & 1)
    else:
        count += sum(score(job)[0] for job in jobs if not len(job) & 1)
    return count


if __name__ == "__main__":
    n = int(input())
    jobs = [input() for _ in range(n)]
    print(simple(jobs))
