#!/usr/bin/env python3

def proc(xs, n, add=False):
    """Process newline delimited string into list of lists of integers.
    Return sorted list of two item tuples, take N largeset
    [(calories:int, index:int)]
    """
    xs = xs[:-1]
    val = [(sum(int(j) for j in i.split("\n")), k+1) for k, i in enumerate(xs.split("\n\n"))]
    val = sorted(val, reverse=True)[:n]
    if add:
        return sum(i for i, _ in val)
    else:
        return val[:n]


def get_data(fname):
    """read string data from file
    """
    with open(fname, 'r', encoding="utf-8") as fptr:
        return fptr.read()


if __name__ == "__main__":

    # Get data from file
    data = get_data("input/day1_input.txt")

    # Find the top 3 elves with the most calories
    print("Top 3 elves:", proc(data, 3))

    # compute total of top 3
    print("total:", proc(data, 3, True), "calories")
