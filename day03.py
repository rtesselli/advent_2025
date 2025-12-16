def parse_input() -> list[str]:
    with open("data/day03.txt") as f:
        return [line.strip() for line in f.readlines()]


def max_char(s: str) -> str:
    return str(max(int(digit) for digit in s))


def max_joltage(bank: str) -> int:
    max_c = max_char(bank)
    idx_max_c = bank.index(max_c)
    while idx_max_c == len(bank) - 1:
        max_c = max_char(f"{bank[:idx_max_c]}{bank[idx_max_c + 1:]}")
        idx_max_c = bank.index(max_c)
    second_max_c = max_char(bank[idx_max_c + 1:])
    return int(f"{max_c}{second_max_c}")


def max_joltage_rec(bank: str, left_chars: int) -> str:
    if left_chars == 1:
        return max_char(bank)
    max_c = max_char(bank[:-left_chars + 1])
    idx_max_c = bank.index(max_c)
    return max_c + max_joltage_rec(bank[idx_max_c + 1:], left_chars - 1)


def max_joltage2(bank: str) -> int:
    return int(max_joltage_rec(bank, 12))


def part1(banks: list[str]) -> int:
    return sum(max_joltage(bank) for bank in banks)


def part2(banks: list[str]) -> int:
    return sum(max_joltage2(bank) for bank in banks)


if __name__ == '__main__':
    data = parse_input()
    print(part1(data))
    print(part2(data))
