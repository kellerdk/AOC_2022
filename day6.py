#!/usr/bin/env python3

"""Advent of Code - Day 6
"""

def get_data(fname):
    """Get data from text file
    """
    with open(fname, encoding="utf-8") as fptr:
        return fptr.readlines()


def start_detect(xss, num):
    """Detect unique character start sequence, num character long.
    """
    idx = 0
    while len(set(xss[idx:idx+num])) != len(xss[idx:idx+num]):
        idx += 1
    return idx + num


if __name__ == "__main__":

    vals = get_data("input/day6_input.txt")
    _ = [print(start_detect(i, 4)) for i in vals]
    _ = [print(start_detect(i, 14)) for i in vals]
