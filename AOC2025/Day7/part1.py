from AOC2025.aoc_tools import *

@tester(ref_result=40)
def main(lines):
    g = npgrid(lines)
    p = fnpgrid(g, 'S')
    g[p[0]] = '|'

    res = 0
    for i in range(1, g.shape[0]):
        for j in range(g.shape[1]):
            if g[i, j] == '^' and g[i-1, j] == '|':
                res += 1
                if j-1 >=0:
                    g[i, j-1] = '|'
                if j+1 < g.shape[1]:
                    g[i, j+1] = '|'
            elif g[i-1, j] == '|':
                g[i, j] = '|'
    return res
