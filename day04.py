import numpy as np
import scipy


def parse_input() -> np.ndarray:
    with open('data/day04.txt') as f:
        data = np.array([list(line.strip()) for line in f])
    data = np.char.replace(data, '.', '0')
    data = np.char.replace(data, '@', '1')
    return data.astype(int)


def part1(data: np.ndarray) -> int:
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ])
    conv = scipy.signal.convolve2d(data, kernel, mode="same")
    filtered = conv[data == 1]
    return np.sum(filtered < 4)


if __name__ == '__main__':
    matrix = parse_input()
    print(part1(matrix))
