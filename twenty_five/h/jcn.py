from pathlib import Path
from twenty_five.timer import timeit
from itertools import combinations
import heapq


@timeit
def form_circuits1(junctions):
    def pairs():
        for p1, p2 in combinations(junctions, 2):
            x1, y1, z1 = p1
            x2, y2, z2 = p2
            d = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
            yield (d, p1, p2)

    shortest_pairs = heapq.nsmallest(1000, pairs(), lambda x: x[0])

    circuits = [{p} for p in junctions]

    for _, p1, p2 in shortest_pairs:
        c1 = c2 = None

        for c in circuits:
            if p1 in c:
                c1 = c
            if p2 in c:
                c2 = c
            if c1 and c2:
                break

        if c1 is c2:
            continue

        c1.update(c2)
        circuits.remove(c2)

    circuits = sorted(circuits, reverse=True, key=lambda x: len(x))

    l0, l1, l2 = len(circuits[0]), len(circuits[1]), len(circuits[2])
    # print(l0, l1, l2)

    return l0 * l1 * l2

@timeit
def form_circuits2(junctions):
    def pairs():
        for p1, p2 in combinations(junctions, 2):
            x1, y1, z1 = p1
            x2, y2, z2 = p2
            d = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
            yield (d, p1, p2)

    sorted_pairs = sorted(pairs(), key=lambda x: x[0])

    circuits = [{p} for p in junctions]

    for _, p1, p2 in sorted_pairs:
        c1 = c2 = None

        for c in circuits:
            if p1 in c:
                c1 = c
            if p2 in c:
                c2 = c
            if c1 and c2:
                break

        if c1 is c2:
            continue

        c1.update(c2)
        circuits.remove(c2)

        if len(circuits) == 1:
            # print(p1, p2)
            return p1[0] * p2[0]


if __name__ == "__main__":
    junctions = None
    with open(Path(__file__).parent / "in.txt", "r") as file:
        input = file.read().strip().split("\n")
        junctions = [tuple(map(int, line.split(","))) for line in input]

    print(form_circuits1(junctions))
    print(form_circuits2(junctions))
