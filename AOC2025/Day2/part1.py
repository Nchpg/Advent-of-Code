from AOC2025.aoc_tools import *

@tester(ref_result=1227775554)
def main(lines):
    lines = change_line_delim(lines, ",")
    r = 0
    for l in lines:
        a, b = pl(l, d="-")
        for i in range(a, b+1):
            n = str(i)
            if len(n) % 2 == 1:
                continue
            m = len(n)//2
            if n[:m] == n[m:]:
                r += i

    return r