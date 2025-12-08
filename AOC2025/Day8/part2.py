from AOC2025.aoc_tools import *

def dist(a, b):
    return np.linalg.norm(a-b)

def circuit_merge(circuit, x, y):
    ind = -1
    for j in range(len(circuit)):
        if y in circuit[j] and x not in circuit[j]:
            ind = j
            break
    if ind >= 0:
        for j in range(len(circuit)):
            if x in circuit[j]:
                circuit[j] |= circuit[ind]
                del circuit[ind]
                break


@tester(ref_result=25272)
def main(lines):
    coords = np.array(pll(lines, d=','))
    nb_pts = coords.shape[0]
    distance = np.full((nb_pts, nb_pts), np.inf)
    for i in range(nb_pts):
        for j in range(i+1, nb_pts):
            distance[i, j] =  np.linalg.norm(coords[i] - coords[j])

    circuit = [{c} for c in range(nb_pts)]
    while True:
        ind = np.argmin(distance)
        y, x = ind % nb_pts, ind // nb_pts
        circuit_merge(circuit, x, y)
        if len(circuit) == 1:
            return coords[x][0] * coords[y][0]
        distance[x, y] = np.inf


