from AOC2025.aoc_tools import *
import itertools

@tester(ref_result=24)
def main(lines):
    coords = np.array(pll(lines, d=','))
    g = np.full((np.max(coords, axis=0) + (1,1)), ".")

    for i, (x, y) in tqdm(enumerate(coords)):
        g[x, y] = "#"

    for (x1, y1), (x2, y2) in tqdm(zip(coords, np.roll(coords, shift=1, axis=0))):
        dx = 1 if x1 < x2 else -1
        dy = 1 if y1 < y2 else -1
        for x in range(x1, x2+dx, dx):
            for y in range(y1, y2+dy, dy):
                if g[x, y] == ".":
                    g[x, y] = "X"

    m = 0
    for c1, c2 in tqdm(itertools.combinations(coords, 2)):
        x1, y1 = c1
        x2, y2 = c2
        xl = min(x1, x2)
        xh = max(x1, x2)
        yl = min(y1, y2)
        yh = max(y1, y2)
        if abs(xh - xl + 1) * abs(yh - yl + 1) <= m:
            continue
        for c in coords:
            x, y = c
            if np.any(c != c1) and np.any(c != c2) and xl < x < xh  and yl < y < yh:
                break
        else:
            h = g[xl+1:xh, (yl+yh+1)//2]
            if np.any(h != "."):
                continue
            v = g[(xl+xh+1)//2, yl+1:yh]
            if np.any(v != "."):
                continue
            m = max(m, abs(xh - xl + 1) * abs(yh - yl + 1))
    return m
