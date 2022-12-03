#!/usr/bin/env python3

lower = {chr(i+ord('a')): i+1 for i in range(26)}
upper = {chr(i+ord('A')): i+27 for i in range(26)}
priority = {**lower, **upper}

def get_data(fname):
    with open(fname) as fptr:
        return [i.rstrip("\n") for i in fptr.readlines()]

def common_line(s):
    l = len(s)//2
    return priority[list(set(s[:l]) & set(s[l:]))[0]]

def sumpriority(xs):
    return sum(common_line(i) for i in xs)

def common_triple(x, y, z):
    return priority[list(set(x) & set(y) & set(z))[0]]

def sumtriple(xs):
    ys = list(zip(*[xs[i::3] for i in range(3)]))
    return sum(common_triple(*i) for i in ys)


xs = get_data("input/day3_input.txt")
print("by line", sumpriority(xs))
print("by triple", sumtriple(xs))
