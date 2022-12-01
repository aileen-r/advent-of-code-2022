import sys


def parse(puzzle_input):
    """Parse input."""

    elves = []
    for elf in puzzle_input.split("\n\n"):
        elves.append(list(map(lambda x: int(x), elf.split("\n"))))
    
    return elves


def part1(data):
    """Solve part 1."""

    calories_carried = []
    for carried_item_calories in data:
        calories_carried.append(sum(carried_item_calories))

    return max(calories_carried)


def part2(data):
    """Solve part 2."""

    calories_carried = []
    for carried_item_calories in data:
        calories_carried.append(sum(carried_item_calories))

    top_three = sorted(calories_carried, reverse=True)[:3]
    return sum(top_three)


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
