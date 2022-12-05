#!/usr/bin/env python3

"""AOC 2022 - Day 3
"""

lower = {chr(i+ord('a')): i+1 for i in range(26)}
upper = {chr(i+ord('A')): i+27 for i in range(26)}
priority = {**lower, **upper}


def get_data(fname):
    """Get data from file
    """
    with open(fname, encoding="utf-8") as fptr:
        return [i.rstrip("\n") for i in fptr.readlines()]


def single(css):
    """Compute priority character in a single line in two halves
    """
    char = len(css)//2
    return priority[list(set(css[:char]) & set(css[char:]))[0]]


def triple(xln, yln, zln):
    """Compute priority character from common 3 lines.
    """
    return priority[list(set(xln) & set(yln) & set(zln))[0]]


def sumlines(xss, num, fun):
    """Compute the sum over n lines, with function f
    """
    return sum(fun(*i) for i in zip(*[xss[i::num] for i in range(num)]))


if __name__ == "__main__":
    xxs = get_data("input/day3_input.txt")
    print("by line", sumlines(xxs, 1, single))
    print("by triple", sumlines(xxs, 3, triple))
