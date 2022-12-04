#t!/usr/bin/env python3


def get_data(fname):
    with open(fname) as fp:
        return fp.read().split("\n")[:-1]

def to_range(xs):
    x0, x1 = xs.split("-")
    return set(range(int(x0), int(x1)+1))

def proper_subset(x1, x2):
    u = to_range(x1)
    v = to_range(x2)
    return u.issubset(v) | v.issubset(u)

def subset(x1, x2):
    return list(to_range(x1) & to_range(x2)) != []

def overlap_with(xs, f):
    return sum((f(*i.split(","))) for i in xs if True)


if __name__ == "__main__":
    xs = get_data("input/day4_input.txt")
    print(overlap_with(xs, proper_subset))
    print(overlap_with(xs, subset))
