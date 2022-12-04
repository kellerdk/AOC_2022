#t!/usr/bin/env python3


def get_data(fname):
    with open(fname) as fp:
        return fp.read().split("\n")[:-1]

def to_range(xs):
    x0, x1 = xs.split("-")
    return set(range(int(x0), int(x1)+1))

def subset(x1, x2):
    u = to_range(x1)
    v = to_range(x2)
    return u.issubset(v) | v.issubset(u)

def intersect(x1, x2):
    return list(to_range(x1) & to_range(x2)) != []


xs = get_data("input/day4_input.txt")
print(sum((subset(*i.split(","))) for i in xs if True))
print(sum(intersect(*i.split(",")) for i in xs if True))
