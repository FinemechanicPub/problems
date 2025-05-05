import sys


class Towers:
    def __init__(self, n: int):
        self.xy = [0] * n
        self.xz = [0] * n
        self.yz = [0] * n
        self.bits = [1 << i for i in range(n)]
        self.full = (1 << n) - 1

    def add(self, x: int, y: int, z: int):
        self.xy[x] |= self.bits[y]
        self.xz[x] |= self.bits[z]
        self.yz[y] |= self.bits[z]

    def free(self) -> tuple[int, int, int] | None:
        n = len(self.xy)
        xy = self.xy
        xz = self.xz
        yz = self.yz
        bits = self.bits
        full = self.full
        good_y = [y for y in range(n) if yz[y] != full]
        good_x = [x for x in range(n) if xy[x] != full and xz[x] != full]
        for x in good_x:
            for y in good_y:
                xyz = xz[x] | yz[y]
                if not xy[x] & bits[y] and xyz != full:
                    for z in range(n):
                        if xyz & bits[z] == 0:
                            return x, y, z
        return None


if __name__ == "__main__":
    n, k = map(int, input().split())
    towers = Towers(n)
    for _ in range(k):
        x, y, z = map(int, sys.stdin.readline().split())
        towers.add(x - 1, y - 1, z - 1)
    free = towers.free()
    if free is None:
        print("YES")
    else:
        x, y, z = free
        print("NO")
        print(x + 1, y + 1, z + 1)
