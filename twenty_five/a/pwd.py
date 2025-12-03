from pathlib import Path
from twenty_five.timer import timeit


@timeit
def password1(moves):
    val, count = 50, 0

    for m in moves:
        direction, amount = m[0], int(m[1:])

        if direction == "R":
            val += amount
        elif direction == "L":
            val -= amount

        val %= 100

        if val == 0:
            count += 1

    return count


@timeit
def password2(moves):
    val, count = 50, 0

    for m in moves:
        direction, amount = m[0], int(m[1:])

        for i in range(amount):
            if direction == "R":
                val += 1
            elif direction == "L":
                val -= 1
            val %= 100

            if val == 0:
                count += 1

    return count


if __name__ == "__main__":
    moves = None
    with open(Path(__file__).parent / "in.txt", "r") as file:
        moves = file.read().strip().split("\n")

    print(password1(moves))
    print(password2(moves))
