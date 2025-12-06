from math import prod
from pathlib import Path
from twenty_five.timer import timeit


@timeit
def cephalopod_homework1(worksheet):
    total = 0
    for col in zip(*worksheet):
        a, b, c, d, op = col
        if op == "+":
            total += int(a) + int(b) + int(c) + int(d)
        elif op == "*":
            total += int(a) * int(b) * int(c) * int(d)

    return total


@timeit
def cephalopod_homework2(worksheet):
    op, nums = "", []
    total = 0
    for col in zip(*worksheet):
        if col[-1] in {"+", "*"}:
            op = col[-1]
            nums.append(int("".join(col[0:4]).strip()))
        elif all(c == " " for c in col):
            if op == "+":
                total += sum(nums)
            elif op == "*":
                total += prod(nums)
            op, nums = "", []
        else:
            nums.append(int("".join(col[0:4]).strip()))

    if op == "+":
        total += sum(nums)
    elif op == "*":
        total += prod(nums)

    return total


if __name__ == "__main__":
    worksheet1, worksheet2 = [], []
    with open(Path(__file__).parent / "in.txt", "r") as file:
        worksheet2 = file.read().split("\n")
        for line in worksheet2:
            nums = [n for n in line.split(" ") if n != ""]
            worksheet1.append(nums)

    print(cephalopod_homework1(worksheet1))
    print(cephalopod_homework2(worksheet2))
