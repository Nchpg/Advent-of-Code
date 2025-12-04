from AOC2025.aoc_tools import *

@tester(ref_result=43)
def main(lines):
    g = npgrid(lines)
    r = 0
    r_save = -1
    while r != r_save:
        r_save = r
        for i, j in lnpgrid(g, "@"):
            c = 0
            for di, dj in adj8:
                if cvnpgrid(g, i+di, j+dj, "@"):
                    c+=1
            if c < 4:
                r+=1
                g[i, j] = '.'
    return r
