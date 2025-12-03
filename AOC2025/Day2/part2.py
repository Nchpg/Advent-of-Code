from AOC2025.aoc_tools import *

@tester(ref_result=4174379265)
def main(lines):
    lines = change_line_delim(lines, ",")
    r = 0
    for l in lines:
        a, b = pl(l, d="-")
        for i in range(a, b + 1):
            n = str(i)
            for j in range(1, len(n)//2 + 1):
                if len(n)%j == 0:
                    l = [int(n[x*j:(x+1)*j]) for x in range(len(n)//j)]
                    if all([e == l[0] for e in l]):
                        r += i
                        break

    return r
