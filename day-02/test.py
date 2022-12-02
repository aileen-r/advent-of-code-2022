import pathlib
import pytest
import solve


PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def parse_test_input():
    puzzle_input = (PUZZLE_DIR / "test-input.txt").read_text().strip()
    return solve.parse(puzzle_input)


def test_parse(parse_test_input):
    """Test that input is parsed properly."""
    assert parse_test_input == [["A", "Y"], ["B", "X"], ["C", "Z"]]


def test_scoreForRound_for_each_permutation():
    """Test that scoreForRound does what it's meant to"""
    assert solve.scoreForRound(1, 1) == 3 + 1
    assert solve.scoreForRound(2, 1) == 6 + 2
    assert solve.scoreForRound(3, 1) == 0 + 3
    assert solve.scoreForRound(1, 2) == 0 + 1
    assert solve.scoreForRound(2, 2) == 3 + 2
    assert solve.scoreForRound(3, 2) == 6 + 3
    assert solve.scoreForRound(1, 3) == 6 + 1
    assert solve.scoreForRound(2, 3) == 0 + 2
    assert solve.scoreForRound(3, 3) == 3 + 3

def test_part1(parse_test_input):
    assert solve.part1(parse_test_input) == 15

def test_part2(parse_test_input):
    assert solve.part2(parse_test_input) == 12