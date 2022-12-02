#!/usr/bin/env python3

def proc(xs, n):
    """Process newline delimited string into list of lists of integers.
    Return sorted list of two item tuples, take N largeset
    [(calories:int, index:int)]
    """
    idx = 0
    vals = []
    ret = []
    for i in xs.split("\n"):
        if i == "":
            idx += 1
            ret.append((sum(vals), idx))
            vals = []
        else:
            vals.append(int(i))
    return sorted(ret, reverse=True)[:n]


def get_data(fname):
    """read string data from file
    """
    with open(fname, 'r', encoding="utf-8") as fptr:
        return fptr.read()


if __name__ == "__main__":

    # Get data from file
    data = get_data("input/day1_input.txt")

    # Find the top 3 elves with the most calories
    elves = proc(data, 3)

    # Display those results
    _ = [print(f"{i} calories, ({j})") for i, j in elves]

    # Total up the results from the top three elves
    print(sum((i for i, _ in elves)), "calories total")
