from AOC2025.aoc_tools import *

@tester(ref_result=40)
def main(lines):
    cache = {}

    def forward(i, j):
        if j < 0 or j >= g.shape[1]:
            return 0
        if i >= g.shape[0]:
            return 1
        if (i, j) in cache:
            return cache[(i, j)]
        if g[i, j] == '^':
            cache[(i, j)] = forward(i, j - 1) + forward(i, j + 1)
        else:
            cache[(i, j)] = forward(i + 1, j)
        return cache[(i, j)]

    g = npgrid(lines)
    p = fnpgrid(g, 'S')

    return forward(*p[0])