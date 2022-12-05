#!/usr/bin/env python3

""" AOC 2022
"""

def get_data(fname):
    """Get data from file
    """
    with open(fname, encoding='utf-8') as fptr:
        return fptr.read().split("\n")

def decode(css):
    """decode opponent + outcome
    """
    match(css):
        case "A X": scr = 3  # rock, lose -> scissor -> 0 + 3
        case "A Y": scr = 4  # rock, draw -> rock -> 3 + 1
        case "A Z": scr = 8  # rock, win -> paper -> 6 + 2

        case "B X": scr = 1  # paper, lose -> rock ->  0 + 1
        case "B Y": scr = 5  # paper, draw -> paper ->  3 + 2
        case "B Z": scr = 9  # paper, win -> scissor ->  6 + 3

        case "C X": scr = 2  # scissor, lose -> paper -> 0 + 2
        case "C Y": scr = 6  # scissor, draw -> scissor -> 3 + 3
        case "C Z": scr = 7  # scissor, win -> rock -> 6 + 1
        case _: scr = 0
    return scr

def score(css):
    """Scope match with stratgy
    """
    match (css):
        case "A X": scr = 4  # rock, rock -> tie  -> 1 + 3
        case "A Y": scr = 8  # rock, paper -> win -> 2 + 6
        case "A Z": scr = 3  # rock, scissor -> loose -> 0 + 3

        case "B X": scr = 1  # paper, rock -> loose -> 0 + 1
        case "B Y": scr = 5  # paper, paper -> tie -> 2 + 3
        case "B Z": scr = 9  # paper, scissor -> win -> 3 + 6

        case "C X": scr = 7  # scissor, rock -> win -> 1 + 6
        case "C Y": scr = 2  # scissor, paper -> loose -> 2 + 0
        case "C Z": scr = 6  # scissor, scissor -> tie -> 3 + 3
        case _: scr = 0
    return scr


if __name__ == "__main__":
    print(sum(score(i) for i in get_data("input/day2_input.txt")))
    print(sum(decode(i) for i in get_data("input/day2_input.txt")))
