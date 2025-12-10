from AOC2025.aoc_tools import *
import itertools

@tester(ref_result=50)
def main(lines):
    coords = np.array(pll(lines, d=','))
    return max(abs(x1-x2+1)*abs(y1-y2+1) for (x1, y1), (x2, y2) in itertools.combinations(coords, 2))
