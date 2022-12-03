#!/usr/bin/env python3

def proc(xs, n):
    """Process newline delimited string into list of lists of integers. Return
    sorted list of two item tuples, take N largeset [(calories:int, index:int)]
    """
    return sorted(((sum(int(j) for j in i.split()), k+1)
                   for k, i in enumerate(xs.split("\n\n"))), reverse=True)[:n]


def day1(fname, n):
    """read string data from file, process top 3 items
    """
    with open(fname, 'r', encoding="utf-8") as fptr:
        top = proc(fptr.read(), n)
        print("Top 3 elves:", top)
        print("total:", sum(i for i, _ in top), "calories")


if __name__ == "__main__":
    day1("input/day1_input.txt", 3)
