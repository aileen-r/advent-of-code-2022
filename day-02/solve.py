import sys


def parse(puzzle_input):
    """Parse input."""

    result = list(map(lambda round: round.split(), puzzle_input.split("\n")))
    return result

def scoreForRound(my_move, opponent_move):
        """Returns player's score from a given round in the decrypted_guide"""

        # start with score from shape played
        score = my_move;

        if (opponent_move == my_move):
            # draw
            score += 3
        elif ((opponent_move < my_move or (opponent_move == 3 and my_move == 1)) and not (opponent_move == 1 and my_move == 3)):
            # win
            score += 6

        # 0 for loss

        return score


def part1(guide):
    """Solve part 1."""

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
    for game_round in guide:
        decrypted_guide.append(list(map(lambda x: decryption_dict[x], game_round)))


    result = sum(map(lambda round: scoreForRound(round[1], round[0]), decrypted_guide))

    return result

def getMyMove(opponent_move, desired_outcome):
    """Takes an opponent move (1, 2 or 3), a desired outcome (X, Y, or Z) and returns my ideal move (1, B, or C)"""

    match desired_outcome:
        case "X":
            # lose
            my_move = opponent_move - 1
        case "Y":
            # draw
            my_move = opponent_move
        case "Z":
            # win
            my_move = opponent_move + 1
    
    # circle back around to 1 or 3 if appropriate
    my_move = 1 if my_move > 3 else my_move
    my_move = 3 if my_move < 1 else my_move

    return my_move



def part2(guide):
    """Solve part 2."""

    # rock = 1
    # paper = 2
    # scissors = 3
    shape_decryption = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    def decryptAndGetScoreForRound(round):
        opponent_move = shape_decryption[round[0]]
        desired_outcome = round[1]
        my_move = getMyMove(opponent_move, desired_outcome)
        return scoreForRound(my_move, opponent_move)

    result = sum(map(decryptAndGetScoreForRound, guide))
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