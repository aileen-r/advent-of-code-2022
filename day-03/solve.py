import string
import sys

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input.split("\n")

def splitRucksackIntoCompartments(rucksack):
    contentsPerCompartments = len(rucksack) // 2

    return rucksack[0 : contentsPerCompartments],  rucksack[contentsPerCompartments : len(rucksack)]


def findCommonCharacter(string1, string2, string3=""):
    """Finds the first common character between two strings of the same length."""
    commonCharacter = ""
    for i in range(len(string1)):
        char = string1[i]
        if (string2.find(char) > -1) and ((len(string3) == 0) or (string3.find(char) > -1)):
            commonCharacter = char
            break
    return commonCharacter



def part1(data):
    """Solve part 1."""

    rucksacks = map(splitRucksackIntoCompartments, data)
    commonCharacters = map(lambda rucksack: findCommonCharacter(*rucksack), rucksacks)
    result = sum(map(lambda char: string.ascii_letters.find(char) + 1, commonCharacters))

    return result


def divideRucksacksIntoGroups(rucksacks):
    rucksacksPerGroup = 3
    for i in range(0, len(rucksacks), rucksacksPerGroup):
        yield rucksacks[i:i + rucksacksPerGroup]


def part2(rucksacks):
    """Solve part 2."""

    rucksacksByGroup = divideRucksacksIntoGroups(rucksacks)
    commonCharacters = map(lambda group: findCommonCharacter(*group), rucksacksByGroup)

    result = sum(map(lambda char: string.ascii_letters.find(char) + 1, commonCharacters))
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