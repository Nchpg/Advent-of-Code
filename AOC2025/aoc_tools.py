import numpy as np
from tqdm import tqdm
import re

#GRID OFFSET
adj8 = [[i, j] for i in [-1, 0, 1]  for j in [-1, 0, 1]  if i != 0 or j != 0]
corner = [[i, j] for i in [-1, 0, 1]  for j in [-1, 0, 1]  if abs(i)+abs(j) == 2]
cross = [[i, j] for i in [-1, 0, 1]  for j in [-1, 0, 1]  if abs(i)+abs(j) == 1]

def d_tr(dx, dy):
    return dy, -dx

def g_tr(dx, dy):
    return dy, -dx

def change_line_delim(lines, d):
    return ("\n".join(lines)).split(d)

def nums(line):
    return [int(num) for num in re.findall(r'\d+', line)]

def lnums(lines):
    return [nums(l) for l in lines]

#Parse line into list of type t by delimiter d
def pl(l, d="", t=int):
    return list(map(t, l.split(d if d else None)))

#Cast list of type a in list of type t
def cl(l, t=int):
    return list(map(t, l))

#Parse list of line into list of list of type t by delimiter d
def pll(l, d="", t=int):
    return list(map(lambda x: list(map(t, x)), [[a.strip() for a in e.split(d if d else None) if a.strip()] for e in l]))

#Cast list of list of type a in list of list of type t
def cll(l, t=int):
    return list(map(lambda x: list(map(t, x)), [cl(e, t) for e in l if e]))

#Parse list of list in grid of type t
def grid(l, t=str):
    return [[t(a) for a in list(e) if a.strip()] for e in l if e]

def npgrid(l, t=str):
    g = np.array(grid(l, t))
    return g

def cnpgrid(g, i, j):
    return 0 <= i < g.shape[0] and 0 <= j < g.shape[1]

def cvnpgrid(g, i, j, v):
    return cnpgrid(g, i, j) and g[i][j] == v




def pnpgrid(g):
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            yield g[i][j]

def penpgrid(g):
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            yield i, j, g[i][j]

def enpgrid(g):
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            yield i, j

def fnpgrid(g, x):
    f = []
    for i, j in enpgrid(g):
        if g[i][j] == x:
            f.append((i, j))
    return f

def lnpgrid(g, l):
    f = l
    if not isinstance(l, type(lambda x:x)):
        if list == type(l):
            f = lambda x : x in l
        else:
            f = lambda x: x == l
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            if f(g[i][j]):
                yield i, j


def print_grid(g):
    print("="*g.shape[1])
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            print(g[i][j], end="")
        print()
    print("="*g.shape[1])

def tqdm_enpgrid(g):
    return tqdm(enpgrid(g), total=g.shape[0] * g.shape[1])

def tqdm_pnpgrid(g):
    return tqdm(pnpgrid(g), total=g.shape[0] * g.shape[1])

def tqdm_penpgrid(g):
    return tqdm(penpgrid(g), total=g.shape[0] * g.shape[1])

def tqdm_lnpgrid(g, l):
    return tqdm(lnpgrid(g, l), total=g.shape[0] * g.shape[1])

def linear_solve(A, Y):
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square (number of rows must equal number of columns).")
    if A.shape[0] != Y.shape[0]:
        raise ValueError("The number of rows in A must match the number of rows in Y.")
    try:
        X = np.linalg.solve(A, Y)
        return X
    except np.linalg.LinAlgError as e:
        raise np.linalg.LinAlgError(f"Matrix A is singular or not invertible: {e}")


def tester(ref_result=None):
    import ast
    import sys
    import pyperclip
    import time
    sys.setrecursionlimit(10 ** 6)

    def wrapper(func):
        def main(filename):
            with open(filename, "r") as file:
                lines = file.read().splitlines()
                if len(lines) == 0:
                    print(f"\033[1mFile {filename} is empty\033[0m")
                    if filename == "ref":
                        return True, "", "", True
                    print("Killed")
                    exit(0)
                ref = ""
                if filename == "ref":
                    ref = ref_result
                res = func(lines)
                if res is None:
                    res = "NaN"
                time.sleep(0.1)
                print(end=" ", flush=True)
                _type = None
                if type(res) == tuple and len(res) == 2:
                    if res[1] in [int, float, tuple, list, str]:
                        current, _type = res[0], res[1]
                    else:
                        print(f"\033[1mType ({res[2]}) not taken\033[0m")
                        current = res
                else:
                    current = res
                if ref != "":
                    if _type is not None:
                        if _type == list or _type == tuple:
                            ref = ast.literal_eval(ref)
                        else:
                            ref = _type(ref)
                        return ref == current, current, ref, False
                    if type(current) == list or type(current) == tuple:
                        ref = ast.literal_eval(ref)
                    else:
                        ref = type(current)(ref)

                    return ref == current, current, ref, False
                return True, current, "", False

        pyperclip.copy("")
        if ref_result:
            b, current, ref, ignored = main("ref")
            if ignored:
                print(f"--> Ref was ignored ⭕\n")
            elif b:
                print(f"\n--> Ref is valid ✅ : expected \033[1m{ref}\033[0m, get \033[1m{current}\033[0m\n")
            else:
                print(
                    f"\n--> Ref is not valid ❌ : expected \033[1m{ref}\033[0m (type: {type(ref)}), get \033[1m{current}\033[0m (type: {type(current)})")
                print("Killed")
                exit(0)
        b, current, _, _ = main("input")
        if b:
            print(f"--> Result is \033[1m{current}\033[0m")
            pyperclip.copy(current)
    return wrapper
