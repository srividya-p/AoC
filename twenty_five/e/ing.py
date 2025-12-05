from pathlib import Path
from twenty_five.timer import timeit


@timeit
def count_fresh1_bruteforce(fresh, ingredients):
    total = 0
    for i in ingredients:
        for j in range(len(fresh)):
            if fresh[j][0] <= i <= fresh[j][1]:
                total += 1
                break
    return total


@timeit
def count_fresh1_optimised(fresh, ingredients):
    # Sort and merge intervals to make them disjoint
    fresh_sorted = sorted(fresh, key=lambda f: (f[0], f[1]))
    fresh_merged = [fresh_sorted[0]]
    for current in fresh_sorted[1:]:
        last_merged = fresh_merged[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(current[1], last_merged[1])
        else:
            fresh_merged.append(current)

    # Binary search to find the correct interval start
    total = 0
    N = len(fresh_merged)
    for target in ingredients:
        left, right = 0, N - 1
        target_start_i = 0
        while left <= right:
            mid = (left + right) // 2

            if fresh_merged[mid][0] <= target:
                target_start_i = mid
                left = mid + 1
            else:
                right = mid - 1
        if fresh_merged[target_start_i][0] <= target <= fresh_merged[target_start_i][1]:
            total += 1
    return total


@timeit
def count_fresh2(fresh):
    # Sort and merge intervals to make them disjoint
    fresh_sorted = sorted(fresh, key=lambda f: (f[0], f[1]))
    fresh_merged = [fresh_sorted[0]]
    for current in fresh_sorted[1:]:
        last_merged = fresh_merged[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(current[1], last_merged[1])
        else:
            fresh_merged.append(current)

    total = 0
    for f in fresh_merged:
        total += f[1] - f[0] + 1

    return total


if __name__ == "__main__":
    fresh, ingredients = [], []
    with open(Path(__file__).parent / "in.txt", "r") as file:
        input = file.read().strip().split("\n")
        for line in input:
            if line == "":
                continue
            elif "-" in line:
                fresh.append(list(map(int, line.split("-"))))
            else:
                ingredients.append(int(line))

    print(count_fresh1_bruteforce(fresh, ingredients))
    print(count_fresh1_optimised(fresh, ingredients))

    print(count_fresh2(fresh))
