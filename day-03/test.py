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

    assert list(parse_test_input) == ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]


def test_part1(parse_test_input):
    assert solve.part1(parse_test_input) == 157

def test_part2(parse_test_input):
    assert solve.part2(parse_test_input) == 70