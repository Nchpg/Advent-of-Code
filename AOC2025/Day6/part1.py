from AOC2025.aoc_tools import *

@tester(ref_result=4277556)
def main(lines):
    map_op = {
        "*": (1, lambda x, y: x*y),
        "+": (0, lambda x, y: x+y)
    }
    g = np.array(pll(lines[:-1], d=" ")).T
    op = lines[-1].split()

    res = 0
    for k, l in zip(op, g):
        (z, o) = map_op[k]
        r = z
        for n in l:
            r = o(r, n)
        res += r
    return res