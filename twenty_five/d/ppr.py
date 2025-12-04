from pathlib import Path
from twenty_five.timer import timeit

DIRECTIONS = [
    (0, -1),  # left
    (0, 1),  # right
    (-1, 0),  # top
    (1, 0),  # bottom
    (-1, -1),  # top-left
    (-1, 1),  # top-right
    (1, -1),  # bottom-left
    (1, 1),  # bottom-right
]


@timeit
def forklift1(layout):
    R, C = len(layout), len(layout[0])
    total = 0
    for i in range(R):
        for j in range(C):
            if layout[i][j] == ".":
                continue

            # Check neighbors
            paper_count = 0
            for dr, dc in DIRECTIONS:
                nr, nc = i + dr, j + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if layout[nr][nc] == "@":
                        paper_count += 1
                    if paper_count >= 4:
                        break

            if paper_count <= 3:
                total += 1
    return total


@timeit
def forklift2_bruteforce(layout):
    def get_accessible():
        R, C = len(layout), len(layout[0])
        accessible = []
        for i in range(R):
            for j in range(C):
                if layout[i][j] == ".":
                    continue

                # Check neighbors
                paper_count = 0
                for dr, dc in DIRECTIONS:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        if layout[nr][nc] == "@":
                            paper_count += 1
                        if paper_count >= 4:
                            break

                if paper_count <= 3:
                    accessible.append((i, j))
        return accessible

    def remove_accessible(accessible):
        for r, c in accessible:
            layout[r][c] = "."

    total = 0
    while True:
        accessible = get_accessible()
        if not accessible:
            break
        remove_accessible(accessible)
        total += len(accessible)

    return total

@timeit
def forklift2_optimized(layout):
    queue = []
    counts = [[0] * len(layout[0]) for _ in range(len(layout))]
    R, C = len(layout), len(layout[0])

    # Init BFS queue and counts
    for i in range(R):
        for j in range(C):
            if layout[i][j] == ".":
                continue

            # Check neighbors
            paper_count = 0
            for dr, dc in DIRECTIONS:
                nr, nc = i + dr, j + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if layout[nr][nc] == "@":
                        paper_count += 1
            if paper_count <= 3:
                queue.append((i, j))
            counts[i][j] = paper_count

    # BFS on each accessible paper
    total = 0

    while queue:
        r, c = queue.pop(0)
        layout[r][c] = "."

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if layout[nr][nc] == "@":
                    counts[nr][nc] -= 1
                    if counts[nr][nc] == 3:
                        queue.append((nr, nc))
        total += 1

    return total


if __name__ == "__main__":
    layout = None
    with open(Path(__file__).parent / "in.txt", "r") as file:
        layout = file.read().strip().split("\n")
        layout = [list(line) for line in layout]

    print(forklift1(layout))

    # print(forklift2_bruteforce(layout))
    print(forklift2_optimized(layout))