import sys

def parse(puzzle_input):
    """Parse input."""

    result = list(map(lambda round: round.split(","), puzzle_input.split("\n")))
    return result


def getRangeTupleFromAssignment(assignment):
    """Takes a single elf's assignment e.g '2-9' and converts to range(2,9)"""
    start, stop = assignment.split("-")
    return int(start), int(stop)

def isRangeInOtherRange(range1, range2):
    """True if range1 is entirely contained within range2 or vice versa"""

    return ((range1[0] >= range2[0]) and (range1[1] <= range2[1])) or ((range2[0] >= range1[0]) and (range2[1] <= range1[1]))

def doRangesOverlap(range1, range2):
    return (range1[0] <= range2[0] <= range1[1]) or (range2[0] <= range1[0] <= range2[1])

def part1(pairs):
    """Solve part 1."""

    result = 0
    for pairAssignments in pairs:
        ranges = map(getRangeTupleFromAssignment, pairAssignments)
        if isRangeInOtherRange(*ranges):
            result += 1
    return result


def part2(pairs):
    """Solve part 2."""

    result = 0
    for pairAssignments in pairs:
        ranges = map(getRangeTupleFromAssignment, pairAssignments)
        if doRangesOverlap(*ranges):
            result += 1
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