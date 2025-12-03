from pathlib import Path
from twenty_five.timer import timeit

BATS = 100


@timeit
def joltage1(banks):
    total = 0
    for bank in banks:
        max_bat, max_i = bank[0], 0
        for i in range(1, BATS - 1):
            if bank[i] > max_bat:
                max_bat = bank[i]
                max_i = i
        digit1 = max_bat

        max_i += 1
        max_bat = bank[max_i]
        for i in range(max_i, BATS):
            if bank[i] > max_bat:
                max_bat = bank[i]
        digit2 = max_bat

        total += int(digit1 + digit2)

    return total


@timeit
def joltage2(banks):
    SELECT = 12

    total = 0
    for bank in banks:
        mono = []
        skip = BATS - SELECT

        for b in bank:
            while mono and b > mono[-1] and skip > 0:
                mono.pop()
                skip -= 1
            mono.append(b)

        total += int("".join(mono[:SELECT]))

    return total


if __name__ == "__main__":
    banks = None
    with open(Path(__file__).parent / "in.txt", "r") as file:
        banks = file.read().strip().split("\n")

    print(joltage1(banks))
    print(joltage2(banks))
