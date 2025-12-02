def sum_id1(ranges):
    def is_repeating_1(n):
        s = str(n)
        if len(s) % 2 != 0:
            return False
        mid = len(s) // 2
        return s[:mid] == s[mid:]

    total = 0
    for r in ranges:
        for n in range(r[0], r[1] + 1):
            if is_repeating_1(n):
                total += n
    return total


def sum_id2(ranges):
    def is_repeating_2(n):
        s = str(n)
        rep = s + s
        strip = rep[1:-1]
        return s in strip

    total = 0
    for r in ranges:
        for n in range(r[0], r[1] + 1):
            if is_repeating_2(n):
                total += n
    return total


if __name__ == "__main__":
    ranges = None
    with open("in.txt", "r") as file:
        ranges = file.read().strip().split(",")
        ranges = [tuple(map(int, r.split("-"))) for r in ranges]

    print(sum_id1(ranges))
    print(sum_id2(ranges))
