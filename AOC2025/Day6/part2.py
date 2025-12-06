from AOC2025.aoc_tools import *

@tester(ref_result=3263827)
def main(lines):
    map_op = {
        "*": (1, lambda x, y: x*y),
        "+": (0, lambda x, y: x+y)
    }

    l = lines[:-1]
    max_len = max(len(l[i]) for i in range(len(l)))
    g = [[]]

    for j in range(max_len):
        nb = -1
        for i in range(len(l)):
            if len(l[i]) <= j:
                continue
            if ord(l[i][j]) in range(ord('0'), ord('9')+1):
                nb = max(0,nb)*10 + int(l[i][j])
            elif nb != -1:
                break
        if nb == -1:
            g.append([])
        else:
            g[-1].append(nb)

    op = lines[-1].split()

    res = 0
    for k, l in zip(op, g):
        (z, o) = map_op[k]
        r = z
        for n in l:
            r = o(r, n)
        res += r
    return res