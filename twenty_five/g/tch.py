from copy import deepcopy
from pathlib import Path
from twenty_five.timer import timeit


@timeit
def analyze_beams(splitters):
    R, C = len(splitters), len(splitters[0])
    split_count = 0

    for i in range(R):
        for j in range(C):
            val = splitters[i][j]
            if val == ".":
                continue
            elif val == "S":
                splitters[i + 1][j] = "|"
            elif val == "^":
                if splitters[i - 1][j] == "|":
                    split_count += 1
                    splitters[i][j - 1] = "|"
                    splitters[i][j + 1] = "|"
                    splitters[i + 1][j - 1] = "|"
                    splitters[i + 1][j + 1] = "|"
            elif val == "|":
                if i + 1 < R and splitters[i + 1][j] == ".":
                    splitters[i + 1][j] = "|"

    return split_count


@timeit
def count_timelines(splitters):
    R, C = len(splitters), len(splitters[0])

    memo = {}

    def explore_timelines(row, col):
        state = (row, col)
        if state in memo:
            return memo[state]

        # Terminating case: Beam has exitted the grid
        if row >= R or row < 0 or col >= C or col < 0:
            return 1  # Count 1 timeline

        cur_char = splitters[row][col]
        result = None

        if cur_char == "^":  # Explore paths to the left or right
            left = explore_timelines(row + 1, col - 1)
            right = explore_timelines(row + 1, col + 1)
            result = left + right
        elif cur_char == ".":  # Explore paths straight down
            down = explore_timelines(row + 1, col)
            result = down

        memo[state] = result
        return result

    source_col = splitters[0].index("S")
    return explore_timelines(
        1, source_col
    )  # We want to start by going down one row from the source


if __name__ == "__main__":
    splitters = []
    with open(Path(__file__).parent / "in.txt", "r") as file:
        input = file.read().strip().split("\n")
        splitters = [list(line) for line in input]

    original_splitters = deepcopy(splitters)
    print(analyze_beams(original_splitters))

    original_splitters = deepcopy(splitters)
    print(count_timelines(original_splitters))
