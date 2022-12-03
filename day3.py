#!/usr/bin/env python3

lower = {chr(i+ord('a')): i+1 for i in range(26)}
upper = {chr(i+ord('A')): i+27 for i in range(26)}
priority = {**lower, **upper}

def get_data(fname):
    with open(fname) as fptr:
        return [i.rstrip("\n") for i in fptr.readlines()]

def single(s):
    l = len(s)//2
    return priority[list(set(s[:l]) & set(s[l:]))[0]]

def triple(x, y, z):
    return priority[list(set(x) & set(y) & set(z))[0]]

def sumlines(xs, n, f):
    return sum(f(*i) for i in zip(*[xs[i::n] for i in range(n)]))


if __name__ == "__main__":
    xs = get_data("input/day3_input.txt")
    print("by line", sumlines(xs, 1, single))
    print("by triple", sumlines(xs, 3, triple))
