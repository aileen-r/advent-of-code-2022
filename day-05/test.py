import pathlib
import pytest
import solve


PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def parse_test_input():
    puzzle_input = (PUZZLE_DIR / "test-input.txt").read_text()
    return solve.parse(puzzle_input)


def test_parse(parse_test_input):
    """Test that input is parsed properly."""

    assert parse_test_input == (["    [D]    ", "[N] [C]    ", "[Z] [M] [P]"], ["move 1 from 2 to 1", "move 3 from 1 to 3", "move 2 from 2 to 1", "move 1 from 1 to 2"], 3)


def test_part1(parse_test_input):
    assert solve.part1(parse_test_input) == "CMZ"

def test_part2(parse_test_input):
    assert solve.part2(parse_test_input) == None