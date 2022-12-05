#!/usr/bin/env python3

""" AOC 2022 - Day 5
"""

import re

repat = re.compile(r"\d+")


def get_data(fname):
    """Get data from input file
    """
    with open(fname, encoding="utf-8") as fptr:
        return fptr.read().split("\n")[:-1]


def crates():
    """
            [J]         [B]     [T]
            [M] [L]     [Q] [L] [R]
            [G] [Q]     [W] [S] [B] [L]
    [D]     [D] [T]     [M] [G] [V] [P]
    [T]     [N] [N] [N] [D] [J] [G] [N]
    [W] [H] [H] [S] [C] [N] [R] [W] [D]
    [N] [P] [P] [W] [H] [H] [B] [N] [G]
    [L] [C] [W] [C] [P] [T] [M] [Z] [W]
     1   2   3   4   5   6   7   8   9
     """
    cdx = {}
    cdx[1] = 'DTWNL'
    cdx[2] = 'HPC'
    cdx[3] = 'JMGDNHPW'
    cdx[4] = 'LQTNSWC'
    cdx[5] = 'NCHP'
    cdx[6] = 'BQWMDNHT'
    cdx[7] = 'LSGJRBM'
    cdx[8] = 'TRBVGWNZ'
    cdx[9] = 'LPNDGW'
    return {k: list(v) for k, v in cdx.items()}


def move_crates(state, moves):
    """Move crates one at a time. FIFO semantics
    """
    for qty, src, dst in moves:
        while qty > 0:
            state[dst] = list(state[src].pop(0)) + state[dst]
            qty -= 1


def move_stack(state, moves):
    """Move crates by stack of crates in one move. FILO semantics
    """
    for qty, src, dst in moves:
        state[dst] = state[src][:qty] + state[dst]
        state[src] = state[src][qty:]


def report_state(state):
    """Report the final string state of the crates
    """
    return "".join(v[0] for v in state.values())


def parse_move(xss):
    """Move description in the form:  (quantity, source, destination)
    """
    return [int(i) for i in repat.findall(xss)]


def parse_moves(xss):
    """Parse move list
    """
    moves = [parse_move(i) for i in xss]
    return [i for i in moves if i]


if __name__ == "__main__":
    directions = get_data("input/day5_input.txt")[9:]
    m = parse_moves(directions)

    for apply in [move_crates, move_stack]:
        s = crates()
        apply(s, m)
        print(f"{apply.__name__}:", report_state(s))
