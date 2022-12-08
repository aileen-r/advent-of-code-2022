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

    assert list(parse_test_input) == [["2-4", "6-8"], ["2-3", "4-5"], ["5-7", "7-9"], ["2-8", "3-7"], ["6-6", "4-6"], ["2-6", "4-8"]]


def test_part1(parse_test_input):
    assert solve.part1(parse_test_input) == 2

def test_part2(parse_test_input):
    assert solve.part2(parse_test_input) == None