def parse_input() -> list[tuple[str, int]]:
    with open("data/day01.txt") as f:
        lines = f.readlines()
    return [
        (line[0], int(line[1:]))
        for line in lines
    ]


def day01_part1(values: list[tuple[str, int]]) -> int:
    curr = 50
    zero_counts = 0
    for direction, value in values:
        if direction == 'R':
            curr += value
        else:
            curr -= value
        curr = curr % 100
        zero_counts += curr == 0
    return zero_counts


if __name__ == '__main__':
    data = parse_input()
    print(day01_part1(data))
