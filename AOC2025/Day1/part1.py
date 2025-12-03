from AOC2025.aoc_tools import *

@tester(ref_result=3)
def main(lines):
    v = 50
    passwd = 0
    m = {"R": lambda x: (v + x) % 100,
         "L": lambda x: (v - x) % 100}
    for l in lines:
        v = m[l[0]](int(l[1:]))
        passwd += (v == 0)
    return passwd
