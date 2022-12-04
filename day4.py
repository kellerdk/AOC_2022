#t!/usr/bin/env python3

def get_data(fname):
    with open(fname) as fp:
        return fp.read().split("\n")[:-1]

def to_range(xs):
    x0, x1 = xs.split("-")
    return set(range(int(x0), int(x1)+1))

def superset(x1, x2):
    u, v = to_range(x1), to_range(x2)
    return u.issubset(v) | v.issubset(u)

def subset(x1, x2):
    return to_range(x1) & to_range(x2) != set()

def overlap_with(xs, f):
    return sum((f(*i.split(","))) for i in xs if True)


if __name__ == "__main__":
    xs = get_data("input/day4_input.txt")
    print("Superset", overlap_with(xs, superset))
    print("Subset:", overlap_with(xs, subset))
