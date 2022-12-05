#!/usr/bin/env python3

import re

repat = re.compile(r"\d+")


def get_data(fname):
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
    cd = {}
    cd[1] = 'DTWNL'
    cd[2] = 'HPC'
    cd[3] = 'JMGDNHPW'
    cd[4] = 'LQTNSWC'
    cd[5] = 'NCHP'
    cd[6] = 'BQWMDNHT'
    cd[7] = 'LSGJRBM'
    cd[8] = 'TRBVGWNZ'
    cd[9] = 'LPNDGW'
    return {k:list(v) for k,v in cd.items()}

def crates_test():
    """
        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3
    """
    cd = {}
    cd[1] = 'NZ'
    cd[2] = 'DCM'
    cd[3] = 'P'
    return {k: list(v) for k, v in cd.items()}


def move_crates(state, moves):
    moves = [i for i in moves if i]
    for qty, src, dst in moves:
        while qty > 0:
            state[dst] = list(state[src].pop(0)) + state[dst]
            print(state)
            qty -= 1


def report_state(state):
    return {k:v[0] for k, v in  state.items()}


def moves_test():
    return """move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2
    """

def parse_move(xs):
    """Move description in the form:  (quantity, source, destination)
        - move 1 from 1 to 2  ->  (1, 1, 2)
    """
    return [int(i) for i in repat.findall(xs)]


def parse_moves(xs):
    #return [parse_move(i) for i in xs.split("\n")]
    return [parse_move(i) for i in xs]

if __name__ == "__main__":
    moves = get_data("input/day5_input.txt")[9:]
    m = parse_moves(moves)
    s = crates()
    move_crates(s, m)
    print("".join(report_state(s).values()))

