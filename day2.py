#!/usr/bin/env python3


def get_data(fname):
    with open(fname) as fp:
        return fp.read().split("\n")

def decode(cs):
    match(cs):
        # A rock -> 1
        # B paper -> 2
        # C scissor -> 3

        # X -> lose -> 0
        # Y -> draw -> 3
        # z -> win -> 6

        case "A X": s = 3  # rock, lose -> scissor -> 0 + 3
        case "A Y": s = 4  # rock, draw -> rock -> 3 + 1
        case "A Z": s = 8  # rock, win -> paper -> 6 + 2

        case "B X": s = 1  # paper, lose -> rock ->  0 + 1
        case "B Y": s = 5  # paper, draw -> paper ->  3 + 2
        case "B Z": s = 9  # paper, win -> scissor ->  6 + 3

        case "C X": s = 2  # scissor, lose -> paper -> 0 + 2
        case "C Y": s = 6  # scissor, draw -> scissor -> 3 + 3
        case "C Z": s = 7  # scissor, win -> rock -> 6 + 1
        case _: s = 0
    return s

def score(cs):
    match (cs):
        # A, X: rock -> 1
        # B, Y: paper -> 2
        # C, Z: scissor -> 3

        # win -> 6
        # tie -> 3
        # lose -> 0

        case "A X": s = 4  # rock, rock -> tie  -> 1 + 3
        case "A Y": s = 8  # rock, paper -> win -> 2 + 6
        case "A Z": s = 3  # rock, scissor -> loose -> 0 + 3

        case "B X": s = 1  # paper, rock -> loose -> 0 + 1
        case "B Y": s = 5  # paper, paper -> tie -> 2 + 3
        case "B Z": s = 9  # paper, scissor -> win -> 3 + 6

        case "C X": s = 7  # scissor, rock -> win -> 1 + 6
        case "C Y": s = 2  # scissor, paper -> loose -> 2 + 0
        case "C Z": s = 6  # scissor, scissor -> tie -> 3 + 3
        case _: s = 0
    return s


print(sum(score(i) for i in get_data("input/day2_input.txt")))
print(sum(decode(i) for i in get_data("input/day2_input.txt")))
