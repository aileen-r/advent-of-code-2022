# Advent of Code 2022

This year I'm trying to brush up on my Python skills, which have not been touched since my degree project in 2017.

## Day 01

Simple problem, but my memories of Python have gone. I am flipping to Google every 2 minutes or so to search for _literally. everything_. A snapshot:

![Screenshot of my ridiculous noob Google searches](./media/google-searches.png)

## Day 02

Having hell with this one. I didn't expect to need to learn to unit test in Python so soon but here we are. It's for the best.

I'm using [pytest](https://docs.pytest.org/en/7.2.x/) and the documentation font is _Garamond_. 😧 My eyes!

After implementing the test for `scoreForRound` it was immediately obvious that my `and not (opponent_score == 1 and my_score == 3)` clause wasn't executing as expected. I needed an extra set of brackets. 🤦🏻‍♀️

That was painful. Lessons learned:
- unit testing speeds up debugging
- when in doubt, use extra brackets for complex conditionals

## Day 03

Pretty simple. Wasted some time asserting against a wrong value in my `parse` unit test.

Learned:
- `return variable1, variable2` returns a tuple.
- `/` division always returns a float in Python 3. `//` can be used to return an integer.
- first brush with generators, which seem to be used a lot in the Python community.

## Day 04
Started working with ranges proper, but by part 2 figured out they don't need enumerated and worked with tuples of the range start/stops instead.

By switching to tuples in part 2 I lost my string-to-int cast for a while: test data was passing but real input was returning different results.

Learned:
- greater/less than comparitors of string representations of numbers do not work.

## Day 05
I had some difficulty in parsing out the stacks of crates. In trying to convert from rows to columns, I was attempting to start with a list of empty lists, then loop over each crate and insert into the list of empty lists at the correct index. For some reason though the list `.append` method was inserting into every list in the list.

One thing I've found is I'm struggling to write the correct search terms for Google with Python problems. I eventually solved this problem by Googling "list insert affecting all lists in nested list" and finding [this Stack Overflow answer](https://stackoverflow.com/a/240205).

## How to run

### Prerequisites

- Install Python
- Install [pytest](https://docs.pytest.org) with `pip install pytest`.

### Running the day's solution
1. `cd` into the directory of the day's problem, e.g. `cd day-01/`.
2. Run `python ./solve.py`
    - Add the `-test` option to run the solution with the test input.

### Running the day's unit tests
1. `cd` into the directory of the day's problem, e.g. `cd day-01/`.
2. Run `python -m pytest ./test.py`.