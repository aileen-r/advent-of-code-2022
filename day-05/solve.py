import re
import sys

def parse(puzzle_input):
    """Parse input."""

    crates = []
    moves = []
    stackCount = 0
    for line in puzzle_input.split("\n"):
        strippedLine = line.strip()
        if (strippedLine).startswith("["):
            crates.append(line)
        elif strippedLine.startswith("move"):
            moves.append(line)
        elif strippedLine.startswith("1"):
            stackCount = int(strippedLine[-1])


    return crates, moves, stackCount

def getStackedCrates(crates, stackCount):
    stackedCrates = [[] for _ in range(stackCount)]
    crates.reverse()
    for rowIdx, row in enumerate(crates):
        for i in range(0, len(row), 4):
            crate = row[i:i+3] if row[i:i+3].strip() else None
            if crate:
                stackedCrates[i//4].insert(rowIdx, crate)
    
    return stackedCrates

def executeMove(move, crates):
    match = re.search(r"move (\d+) from (\d+) to (\d+)", move)
    quantity = match.group(0)
    origin = match.group(1)
    destination = match.group(2)


def part1(data):
    """Solve part 1."""

    crates, moves, stackCount = data;

    cratesByStack = getStackedCrates(crates, stackCount)
    

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