from AOC2025.aoc_tools import *

def search(l):
    cache = {}
    l = [int(c) for c in l]
    w = len(l)

    def _search(start, n):
        if (start, n) in cache:
            return cache[(start, n)]
        cache[(start, n)] = 0
        if n == 1:
            cache[(start, n)] = max(l[start:])
        else:
            cache[(start, n)] = max([l[i]*10**(n-1) + _search(i+1, n-1) for i in range(start, w) if w - i >= n])
        return cache[(start, n)]

    return _search(0, 12)


@tester(ref_result=3121910778619)
def main(lines):
    return sum([search(line) for line in tqdm(lines)])

