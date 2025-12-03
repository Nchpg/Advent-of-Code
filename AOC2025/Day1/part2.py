from AOC2025.aoc_tools import *

@tester(ref_result=6)
def main(lines):
    v = 50
    passwd = 0
    m = {"R": lambda x: (v + x),
         "L": lambda x: (v - x)}
    for l in lines:
        passwd += [x%100 for x in map(m[l[0]], range(1, 1+int(l[1:])))].count(0)
        v = m[l[0]](int(l[1:]))
    return passwd
