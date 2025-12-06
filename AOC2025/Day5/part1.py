from AOC2025.aoc_tools import *

@tester(ref_result=3)
def main(lines):
    ranges, ids = change_line_delim(lines, "\n\n")
    ranges = pll(ranges.split(), d="-")
    ids = list(map(int, ids.split()))
    res = 0
    for i in ids:
        for r in ranges:
            if r[0] <= i <= r[1]:
                res += 1
                break
    return res