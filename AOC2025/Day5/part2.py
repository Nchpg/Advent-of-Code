from AOC2025.aoc_tools import *

@tester(ref_result=14)
def main(lines):
    ranges, _ = change_line_delim(lines, "\n\n")
    ranges = pll(ranges.split(), d="-")
    stack = ranges[::-1]

    seen = set()

    res = 0
    while stack:
        r = stack.pop()
        if r[0] > r[1]:
            continue
        for s in seen:
            # s[0] ---- r[0] ---- r[1] ---- s[1]
            if s[0] <= r[0] and r[1] <= s[1]:
                break

            # r[0] ---- s[0] ---- s[1] ---- r[1]
            if r[0] <= s[0] <= s[1] <= r[1]:
                # r[0] ---- s[0] ---- s[1] **** r[1]
                stack.append([s[1] + 1, r[1]])
                # r[0] **** s[0] ---- s[1] ---- r[1]
                stack.append([r[0], s[0] - 1])
                break

            # r[0] ---- s[0] ---- r[1] ---- s[1]
            if r[0] <= s[0] <= r[1]:
                # r[0] **** s[0] ---- r[1] ---- s[1]
                stack.append([r[0], s[0] - 1])
                break

            # s[0] ---- r[0] ---- s[1] ---- r[1]
            if r[0] <= s[1] <= r[1]:
                # s[0] ---- r[0] ---- s[1] **** r[1]
                stack.append([s[1]+1, r[1]])
                break
        else:
            l = r[1] - r[0] + 1
            if l >= 1:
                res += max(l, 0)
                seen.add(tuple(r))
    return res