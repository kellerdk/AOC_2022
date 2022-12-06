#!/usr/bin/env python3

"""Advent of Code - Day 6
"""


def get_data(fname):
    """Get data from text file
    """
    with open(fname, encoding="utf-8") as fptr:
        return fptr.read()


def uniq(xss):
    """return unique keys as string
    """
    return "".join({k: 1 for k in xss}.keys())


def start_detect(xss, num):
    """Detect unique character start sequence, num character long.
    """
    idx = 0
    while uniq(xss[idx:idx+num]) != xss[idx:idx+num]:
        idx += 1
    return idx + num


if __name__ == "__main__":

    vals = get_data("input/day6_input.txt")
    print(start_detect(vals, 4))
    print(start_detect(vals, 14))
