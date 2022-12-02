import sys


def parse(puzzle_input):
    """Parse input."""

    # rock = 1
    # paper = 2
    # scissors = 3
    decryption_dict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    decrypted_guide = []
    for game_round in puzzle_input.split("\n"):
        decrypted_guide.append(list(map(lambda x: decryption_dict[x], game_round.split())))

    return decrypted_guide

def scoreForRound(round):
        """Returns player's score from a given round in the decrypted_guide"""

        my_score = round[1]
        opponent_score = round[0]

        # start with score from shape played
        score = my_score;

        if (opponent_score == my_score):
            # draw
            score += 3
        elif ((opponent_score < my_score or (opponent_score == 3 and my_score == 1)) and not (opponent_score == 1 and my_score == 3)):
            # win
            score += 6

        # 0 for loss

        return score


def part1(decrypted_guide):
    """Solve part 1."""

    result = sum(map(lambda round: scoreForRound(round), decrypted_guide))


    # print(result)
    # print(any(score > 9 for score in result))

    return result

def part2(data):
    """Solve part 2."""



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