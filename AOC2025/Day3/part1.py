from AOC2025.aoc_tools import *

@tester(ref_result=357)
def main(lines):
    r = 0
    for line in lines:
        l = [int(c) for c in line]
        m = 0
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                t = l[i]*10 +l[j]
                if t > m:
                    m = t
        r += m
    return r
