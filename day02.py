def parse_input() -> list[tuple[int, int]]:
    with open("data/day02.txt") as f:
        lines = f.readlines()
    line = lines[0]
    return [
        (int(ranges.split("-")[0]), int(ranges.split("-")[1]))
        for ranges in line.split(",")
    ]


def is_invalid(value: int) -> bool:
    value = str(value)
    if len(value) % 2 == 1:
        return False
    return value[:len(value) // 2] == value[len(value) // 2:]


def invalid_ids(values: list[tuple[int, int]]) -> list[int]:
    return [
        value
        for start, end in values
        for value in range(start, end + 1)
        if is_invalid(value)
    ]


def part1(values: list[tuple[int, int]]) -> int:
    return sum(invalid for invalid in invalid_ids(values))


if __name__ == '__main__':
    data = parse_input()
    print(part1(data))
