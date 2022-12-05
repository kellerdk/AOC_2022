#t!/usr/bin/env python3

"""AOC 2022 - Day 4
"""


def get_data(fname):
    """Get data from file
    """
    with open(fname, encoding="uft-8") as fptr:
        return fptr.read().split("\n")[:-1]


def to_range(xss):
    """Transform string dash seperated range to python range
    """
    xx0, xx1 = xss.split("-")
    return set(range(int(xx0), int(xx1)+1))


def superset(xx1, xx2):
    """Determine if either argumented is a superset of the other
    """
    uuu, vvv = to_range(xx1), to_range(xx2)
    return uuu.issubset(vvv) | vvv.issubset(uuu)


def subset(xx1, xx2):
    """Determine intersection of the arguments
    """
    return to_range(xx1) & to_range(xx2) != set()


def overlap_with(xss, fun):
    """Calculate number of items satisfed by function, f
    """
    return sum((fun(*i.split(","))) for i in xss if i)


if __name__ == "__main__":
    xs = get_data("input/day4_input.txt")
    print("Superset", overlap_with(xs, superset))
    print("Subset:", overlap_with(xs, subset))
