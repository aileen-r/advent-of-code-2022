import string
import sys

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1."""

    result = None
    return result


def part2(rucksacks):
    """Solve part 2."""

    result = None
    return result


def solve(puzzle_input):
    """Solve the puzzle for the given input."""

    data = parse(puzzle_input)
    # print(*data)

    solution1 = part1(data)

    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":

    path = "./test-input.txt" if (sys.argv[1] == "-test" if len(sys.argv) > 1 else None) else "./input.txt"

    print(f"Running solution against '{path}'...")

    with open(path, 'r') as f:
        puzzle_input = f.read()

    # print(puzzle_input)

    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))